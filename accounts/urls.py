from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('edit', views.edit, name='edit'),
    path('edit-password', views.edit_password, name='edit_password'),
    path('password-reset', views.password_reset, name='password_reset'),
    #path(
    #    'password-reset/',
    #    auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
    #    name='password_reset'
    #),
    #o re_path aceita regex da url
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$',views.password_reset_confirm, name='password_reset_confirm'),
    #path('password_reset_confirm/<int:key>', views.password_reset_confirm, name='password_reset_confirm'),
    #path(
    #    'password-reset-done/',
    #    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    #    name='password_reset_done'
    #),
    #path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
]
