# imports
from django.shortcuts import redirect

# log in checked


def auth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # authenticate user send to home page
        if request.user.is_authenticated:
            return redirect('admin-home-page')

        # unauthenticate user send to logIn page
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

# user type


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # verifying user type
            if request.user.is_superuser == True:
                # allowed user
                return view_func(request, *args, **kwargs)
                print('allowed')

            # not allowed user
            else:
                print('Not allowed')
                return redirect('user-home-page')

        return wrapper_func
    return decorator
