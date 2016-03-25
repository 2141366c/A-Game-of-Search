import user
from models import UserProfile
from django.shortcuts import render, render_to_response
from forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from engine.main import show_game_screen
from engine.game import Game
import pickle

#Homepage view
def index(request):
    return render(request, 'zombieGame/index.html')

#Login view
def login(request):
    context_dict = {'boldmessage': "login"}
    return render(request, 'zombieGame/login.html', context_dict)

#Profile view, requires user to be logged in
@login_required
def profile(request):
    days = request.user.userprofile.days
    kills = request.user.userprofile.kills
    people = request.user.userprofile.people
    food = request.user.userprofile.food
    ammo = request.user.userprofile.ammo
    time = request.user.userprofile.time
    profile = request.user.userprofile

    if profile.days > 30:
        profile.survivorBadge = True

    if profile.kills > 50:
        profile.killerBadge = True

    if profile.food > 80:
        profile.staminaBadge = True

    if profile.people > 40:
        profile.partyBadge = True

    context_dict = {'profile': profile, 'days': days, 'kills': kills, 'people': people,
                    'food': food,'ammo': ammo, 'time': time}
    return render(request, 'zombieGame/profile.html', context_dict)

@login_required
def game(request):
    g=Game()
    t=''
    player = request.user.userprofile
    #Can initialise these using player state !!??
    pps = pickle.dumps(g.player_state)
    kills = 0
    days = 0
    food = 3
    ammo = 2
    people = 1
    g.player_state = pickle.loads(pps)


    context_dict = {'player':player, 'game_over':False, 'new_day':False, 'kills':kills, 'food':food, 'days':days, 'ammo': ammo, 'party': people,
                    'player_state': g.player_state }

    if g.is_game_over():
        context_dict['game_over'] = True
    else:
        g.start_new_day()

    if g.is_day_over():
        g.end_day()
        g.start_new_day()

    if context_dict['game_over'] == False and context_dict['new_day'] == False:
        if t == 'MOVE':
            g.take_turn('MOVE')
        elif t == ('ENTER'):
            g.take_turn('ENTER')
        elif t == ('WAIT'):
            g.take_turn('WAIT')
        elif t == ('FIGHT'):
            g.take_turn('FIGHT')
        elif t == ('SEARCH'):
            g.take_turn('SEARCH')
        elif t == ('EXIT'):
            g.take_turn('EXIT')
        elif t ==('RUN'):
            g.take_turn('RUN')

        context_dict = fill_dict(g)
        context_dict['state'] = str(g.player_state)
        context_dict['gstate'] = g.game_state
        context_dict['time'] = g.time_left

    if g.is_game_over():
        context_dict={'game_over':True}
    elif g.is_day_over():
        context_dict={'new_day':True}
        if g.update_state.party<0:
            print "You lost: {0} people".format(abs(g.update_state.party))

        elif g.update_state.party>0:
            print "{0} more people have joined your party".format(g.update_state.party)

        elif g.update_state.ammo > 0:
            print "You found: {0} units of ammo".format(g.update_state.ammo)

        elif g.update_state.ammo < 0:
            print "You used: {0} units of ammo".format(abs(g.update_state.ammo))

        elif g.update_state.food > 0:
            print "You found: {0} units of food".format(g.update_state.food)

        elif g.update_state.food < 0:
            print "You used: {0} units of food".format(abs(g.update_state.food))

        elif g.update_state.kills > 0:
            print "You killed: {0} zombies".format(g.update_state.kills)

        elif g.update_state.days > 0:
            print "New Day: You survived another day!"
    #Put these updates into a dictionary Q pickle ?

    return render(request, 'zombieGame/game.html', context_dict)

def house(request):
    g = Game()
    g.start_new_day() #need to pickle so not resetting up again
    context_dict = house_dict(g)
    return render(request, 'zombieGame/house.html', context_dict)

def house_dict(g):
    context_dict = {'current_house':g.street.get_current_house(),'current_room':g.street.get_current_house().get_current_room()}
    return context_dict


#The main game view, requires user to be logged in
#@login_required
#def startGame(request):
#    g = Game()
 #   g.start_new_day()
 #   #feel like the pickle stuff should be here but where does it go ?
  #  context_dict=fill_dict(g)
   # return render(request, 'zombieGame/game.html', context_dict)

#need to add ammo, partysize, days


#In this view we create a context_dict variable, which we can alter what is outputted to the game.html
#this is only for street used a separate one for house
def fill_dict(g):

   # game_state = g.game_state
    #pps = pickle.dumps(g.player_state)
   # g.player_state = pickle.loads(pps)
    #ps = pickle.dumps(g.street)
    #g.street = pickle.loads(ps)

        context_dict = {'player_state':g.player_state, 'street': g.street, 'house_list': g.street.house_list, 'current_house':g.street.get_current_house(),
                        'turn': g.turn_options(), 'house_num': ['house_no']}
        return context_dict
        i=0
        for i in g.street.house_list:
            context_dict['house_no'].append(i)
            i += 1




#Leaderboards view, requires user to be logged in
@login_required
def leaderboard(request):
     num = [1,2,3,4,5,6,7,8,9,10]
     kills = UserProfile.objects.order_by('-kills')[:10]
     days = UserProfile.objects.order_by('-days')[:10]
     context_dict = {'index':num, 'kills':kills, 'days':days}
     return render(request, 'zombieGame/leaderboard.html', context_dict)

#Register view
def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # profile.user.kills = 0
            # profile.user.survival = 0

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'zombieGame/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

#Login view
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/zombieGame/profile/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'zombieGame/login.html', {})

#Logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombieGame/')