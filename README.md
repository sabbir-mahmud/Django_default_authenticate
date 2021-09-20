# Django_default_authenticate
Dajngo default user authenticate system

full pure django default authenticate system.you can register new account.you can log in your profile.you can update your details.you can change password.you can reset your password with one time token.you can log in with social applications.to used social authenticate system you have to provide app id and app secrect key in setting page.to use reset password you have to provide a valid email and password also keep turn on low secure apps

# if you want to use only accounts application just clone this repo and copy accounts application. install application:
INSTALLED_APPS = [
    'apps.accounts.apps.AccountsConfig',
    'social_django',
]