from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoginForm, BioForm
from .models import Bio
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    items = Bio.objects.all()
    context = {
       "items":items,
    }
    
    return render(request, 'base/main.html', context )


def posts(request):
    return render(request, 'base/posts.html')

def privacy(request):
    return render(request, 'base/privacy.html')

def terms(request):
    return render(request, 'base/terms.html')


def post(request):
    return render(request, 'base/post.html')

def profile(request):
    try:
        bio_instance = Bio.objects.get()
    except Bio.DoesNotExist:
        bio_instance = None
    # form = BioForm()
    if request.method == "POST":
        form = BioForm(request.POST, instance=bio_instance)
        if form.is_valid():
            if bio_instance:
                bio_instance.delete
            form.save()
            return redirect('base:home')
    else:
        form = BioForm(instance=bio_instance)
    return render(request, 'base/profile.html', {'form':form})


def update_profile(request):
    return render(request, 'base/updateProfile.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_user(request):
    if request.user.is_authenticated:
        return redirect("base:home")  # Assuming 'home' is the name of your home view
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("base:profile")  # Assuming 'home' is the name of your home view
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "base/login.html")


def logout_view(request):
    logout(request)

    return redirect('base:login')

