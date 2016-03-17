from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zombie_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^homepage/', include('homepage.urls')),
	url(r'^profiles/', include('profiles.urls')),
	url(r'^leaderboard/', include('leaderboard.urls')),
	url(r'^register/', include('register.urls')),
	#ISSSUES HERE AND LINE ABOVE url(r'^login/register$', views.register, name='register'),
)
