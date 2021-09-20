# imports
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegForm, EditProfile
from .models import *
from django.contrib.auth.decorators import login_required
from .decorator import auth_user, allowed_user

# Create your views here.

# home view

# admin home page


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def adminHome(request):
    return render(request, 'users/admin.html')
# user home page


@login_required(login_url='login')
def userHome(request):
    return render(request, 'users/user.html')

# home view ends
# register view


@auth_user
def RegView(request):
    fm = RegForm()
    if request.method == 'POST':
        fm = RegForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')

    context = {'form': fm}
    return render(request, 'auth/reg.html', context)

# register view ends
# edit profile view


@login_required(login_url='login')
def edit_profile(request):
    user = request.user.profile
    fm = EditProfile(instance=user)
    if request.method == 'POST':
        fm = EditProfile(request.POST, request.FILES, instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('admin-home-page')

    context = {'form': fm}
    return render(request, 'users/editprofile.html', context)


# edit profile view ends
# verify view


def verifyed(request, token):
    user = Profile.objects.filter(token=token).first()
    user.token = ''
    user.verify = True
    user.save()
    return redirect('login')

# verify view ends
# login view


@auth_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            error = 'Email or Password is wrong'
            context = {'errors': error}
            return render(request, 'auth/login.html', context)

        if user is not None:
            if user.profile.verify == True:
                login(request, user)
                return redirect('admin-home-page')
            else:
                return render(request, 'auth/verifymail.html')

    return render(request, 'auth/login.html')


# login view ends
# logout view

def log_out(request):
    logout(request)
    return redirect('login')

# logout view ends
