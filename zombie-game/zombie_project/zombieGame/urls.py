from django.conf.urls import patterns, url
from zombieGame import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # url(r'^login/$', views.login, name='login'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^game/$', views.game, name='game'),
        url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name = 'logout'),
        url(r'^game/WAIT/$', views.wait, name= 'wait'),
        url(r'^turn/(?P<turn_options_slug>[\w\-]+)/$', views.turn, name='turn'),
)
#(?P<turn_name_slug>[\w\-]+)/