from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Game
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return render(request, 'logged_out.html') 

def home(request):
    return render(request, 'home.html')

@login_required
def inventory(request):
    games = Game.objects.all()
    return render(request, 'inventory.html', {'games': games})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
