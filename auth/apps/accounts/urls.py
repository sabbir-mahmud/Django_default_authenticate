# imports
from django.urls import path, include
from django.contrib.auth import views as reset_password
from . import views

# urls
urlpatterns = [
    # admin/users home urls
    path('', views.adminHome, name='admin-home-page'),
    path('users/', views.userHome, name='user-home-page'),
    # login/out/register/verify urls
    path('login/', views.user_login, name='login'),
    # social login
    path('oauth/', include('social_django.urls', namespace='social')),
    path('sign_up/', views.RegView, name='reg'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('accounts/<slug:token>/', views.verifyed, name='verifyed'),
    path('log_out/', views.log_out, name='log_out'),
    # change password
    path('change_password/', reset_password.PasswordChangeView.as_view(template_name='auth/changepass.html'),
         name='password_change'),
    path('change_password_done/', reset_password.PasswordChangeDoneView.as_view(
        template_name='auth/changepassdone.html'), name='password_change_done'),
    # password reset urls
    # reset password email submit page
    path('reset_password/', reset_password.PasswordResetView.as_view(template_name='auth/forgetpass.html'),
         name='reset_password'),

    # reset password email sent page
    path('reset_token_sent/', reset_password.PasswordResetDoneView.as_view(template_name='auth/emailsent.html'),
         name='password_reset_done'),

    # reset password clicked on mail token page
    path('reset/<uidb64>/<token>/', reset_password.PasswordResetConfirmView.as_view(template_name='auth/setnewpass.html'),
         name='password_reset_confirm'),

    # reset password done page
    path('password_reset_complete/', reset_password.PasswordResetCompleteView.as_view(template_name='auth/forgetpassdone.html'),
         name='password_reset_complete'),
]
