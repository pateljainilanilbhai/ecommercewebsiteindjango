from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, logout, login,addaddress
from .forms import useraddaddressform
from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import *
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/addaddress/$', addaddress, name='addaddress'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]