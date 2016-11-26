"""Grind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
# noinspection PyUnresolvedReferences
from django.core.urlresolvers import reverse
from django.contrib import admin
# noinspection PyUnresolvedReferences
from Grind import settings
from django.conf.urls.static import static
from django.conf import settings
# noinspection PyUnresolvedReferences
from django.contrib.auth.views import login, logout

app_name = 'Spartan'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Spartan.views.index', name='index'),
    url(r'^registration/login.html/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^registration/sign_up/$', 'Spartan.views.sign_up', name='register'),
    url(r'^password_reset/$', 'Spartan.views.password_reset', name = 'password_reset'),
    #url(r'^password_reset/done/$', 'Spartan.views.password_reset_done', name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset', name = 'password_reset_confirm'),
    #url(r'^reset/done/$', 'Spartan.views.password_reset_complete', name = 'password_reset_complete'),
    url(r'^registration/logged_out/$', 'Spartan.views.logout', name='logout'),
   #url(r'^registration/password_reset_done.html/$', 'Spartan.views.password_reset_done',name='password_reset_done'),
    url(r'^user/home.html/$', 'Spartan.views.home', name='home'),
    url(r'^user/workout_form/$', 'Spartan.views.workout_form', name='workouts'),
    url(r'^user/meal_form/$', 'Spartan.views.meal_form', name='meals'),
    url(r'^user/edit_meal.html/(?P<meal_id>\w+)/edit/$', 'Spartan.views.edit_meal', name='edit_meal'),
    url(r'^edit_workout.html/(?P<workout_id>\w+)/edit/$', 'Spartan.views.edit_workout', name='edit_workout'),


)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
