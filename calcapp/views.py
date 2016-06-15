from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from calcapp.forms import Mathcalc

# Create your views here.


def view_index(request):
    result = ''
    num_a = ''
    num_b = ''
    math_op = ''
    final_string = ''
    if request.POST:
        form = Mathcalc(request.POST)
        if form.is_valid():
            num_a = form.cleaned_data['num_a']
            num_b = form.cleaned_data['num_b']
            math_op = form.cleaned_data['math_op']
            if math_op == 'add':
                result = num_a + num_b
                final_string = "{} + {} = {}".format(num_a, num_b, result)
            if math_op == 'sub':
                result = num_a - num_b
                final_string = "{} - {} = {}".format(num_a, num_b, result)
            if math_op == 'mult':
                result = num_a * num_b
                final_string = "{} * {} = {}".format(num_a, num_b, result)
            if math_op == 'div':
                result = num_a / num_b
                final_string = "{} / {} = {}".format(num_a, num_b, result)
    return render(request, 'index.html', {'form': Mathcalc(), 'num1': num_a, 'num2': num_b, 'result': result, 'fin': final_string})


def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def use_calc(request):
    return render(request, 'history.html')


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
