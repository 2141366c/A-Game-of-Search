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
    # if user.is_active:
    #     return HttpResponseRedirect('/zombieGame/profile/')
    # else:
    #     return HttpResponseRedirect('/zombieGame/login/')
    return render(request, 'zombieGame/index.html')

def login(request):
    context_dict = {'boldmessage': "login"}
    return render(request, 'zombieGame/login.html', context_dict)

def profile(request):
    context_dict = {'boldmessage': "profile"}
    return render(request, 'zombieGame/profile.html', context_dict)

def game(request):
    g = Game()
    g.start_new_day()
    response = show_game_screen(g)
    return render(response, 'zombieGame/game.html', {})

def leaderboard(request):
    context_dict = {'boldmessage': "leaderboard"}
    #kills_list = kills.objects.order_by('-kills')[:10]
    #survival_list = survival.objects.order_by('-days')[:10]
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

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombieGame/')