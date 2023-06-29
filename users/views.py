from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . models import Profile
from . forms import ProfileForm, UpdateProfileForm

# Create your views here.
# register
def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            cpassword = form.cleaned_data.get('password2')

            if password != cpassword:
                messages.warning(request, 'Password not match')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username already exist')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist')

            user = User.objects.create_user(username,email,password)
            form = form.save(commit = False)
            form.user = user
            form.save()
            messages.success(request, 'registration successful')
            return redirect('index')
    if 'next' in request.GET:
        next_url = request.GET.get('next')
        return redirect('next_url') 

    context={
        'form':form
    } 
    return render(request, 'users/register.html',context)

# login
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            messages.success(request, 'login successful')

            if 'next' in request.GET:
                next_url = request.GET.get('next')
                return redirect('next_url')

            return redirect('dashboard')
        else:
            messages.warning(request, 'Username/Password not match')
    return render(request, 'users/login.html')

# logout
def logout_user(request):
    logout(request)
    messages.success(request, 'logout successful')
    return redirect('login')

# dashboard
@login_required(login_url='login')

def dashboard(request):
    # if request.user.is_authenticated:
    # return redirect('dashboard')

    users = request.user.profile
    context = {
        'users' : users
    }
    return render(request, 'users/dashboard.html', context)

# update
@login_required(login_url='login')
def update(request):
    user = User.objects.get(username=request.user)
    users = request.user.profile
    update = UpdateProfileForm(instance = users)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=users)
        if form.is_valid():
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.save()
            form.save()
            messages.success(request, 'profile update successful')

    context ={
        'users' : user,
        'form' : update
    }
    
    return render(request, 'users/update.html', context)