from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.


def view_index(request):
    return render(request, 'index.html')


def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def use_calc(request):
    return render(request, 'calculator.html')


def create_user(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'createuser.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'createuser.html', {'form': form})


def view_profile(request):
    return render(request, 'profile.html')
