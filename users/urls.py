from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # registrations
    path('register/', views.register, name = 'register'),
    # login
    path('login/', views.login_user, name = 'login'),
    # logout
    path('logout/', views.logout_user, name = 'logout'),
    # dashboard
    path('dashboard/', views.dashboard, name = 'dashboard'),
    # update
    path('update/', views.update, name = 'update'),



    # RESET PASSWORD
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password/reset_password.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password/reset_password_sent.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password/reset_password_confirm.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/reset_password_complete.html'), name ='password_reset_complete'),
]