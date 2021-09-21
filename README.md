# Django_default_authenticate
Dajngo default user authenticate system

full pure django default authenticate system.you can register new account.you can log in your profile.you can update your details.

# reqirments:
1. python venv
2. django
3. pillow
4. social-auth-app-django 4.0.0

# run project:
open terminal and run those commands:
active virtual envirment * .\Scripts\activate * cd email_verify
migrate project * python manage.py makemigrations * python manage.py migrate
run project * python manage.py runserver

# configure email settings:
project settings.py:
Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Yourmail@your.com'
EMAIL_HOST_PASSWORD = 'Your Password'


# if you need superuser/admin
create superuser:
* python manage.py createsuperuser
* enter your email
* enter your password
