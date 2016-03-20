import user
from django.shortcuts import render, render_to_response
from zombieGame.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from engine.main import show_game_screen
from engine.game import Game

def index(request):
    return render(request, 'zombieGame/index.html')

def login(request):
    context_dict = {'boldmessage': "login"}
    return render(request, 'zombieGame/login.html', context_dict)

@login_required
def profile(request):
    context_dict = {'boldmessage': "profile"}
    return render(request, 'zombieGame/profile.html', context_dict)

def fill_dict(g):
    if g.game_state == 'STREET':
        context_dict = {'street': g.street, 'house_list': g.street.house_list,
                        'current_house':g.street.get_current_house()}

    if g.game_state == 'ZOMBIE':
        context_dict = {'street': g.street, 'house_list': g.street.house_list,
                        'current_house':g.street.get_current_house(),
                        'current_room':g.street.get_current_house().get_current_room(),
                        'zombies': g.street.get_current_house().current_room.zombies}
    #i = 0
    #for i in g.street.house_list:

     #   i += 1
    return context_dict

@login_required
def game(request):

    g = Game()
    g.start_new_day()
    context_dict=fill_dict(g)
    return render(request, 'zombieGame/game.html', context_dict)

@login_required
def leaderboard(request):
    context_dict = {'kills_list': user.kills.objects.order_by('-kills')[:10],
                    'survival_list': user.survival.objects.order_by('-days')[:10]}
    return render(request, 'zombieGame/leaderboard.html', context_dict)

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
            #
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

def user_login(request):

    loggedin = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                loggedin = True
                return HttpResponseRedirect('/zombieGame/profile/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'zombieGame/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombieGame/')