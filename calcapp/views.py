from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from calcapp.forms import Mathcalc
from calcapp.models import Calculation

# Create your views here.


def view_index(request):
    # Calculator function
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
                math_opr = '+'
                result = num_a + num_b
                final_string = "{} + {} = {}".format(num_a, num_b, result)
            if math_op == 'sub':
                math_opr = '-'
                result = num_a - num_b
                final_string = "{} - {} = {}".format(num_a, num_b, result)
            if math_op == 'mult':
                math_opr = '*'
                result = num_a * num_b
                final_string = "{} * {} = {}".format(num_a, num_b, result)
            if math_op == 'div':
                math_opr = '/'
                result = num_a / num_b
                final_string = "{} / {} = {}".format(num_a, num_b, result)
        if request.user.is_authenticated():
            user = request.user
            Calculation.objects.create(user=user, num1=num_a, num2=num_b, mathop=math_opr, result=result, finalstring=final_string)
        # mathop=math_op, result=result, finalstring=final_string)
    return render(request, 'index.html', {'form': Mathcalc(), 'num1': num_a, 'num2': num_b, 'result': result, 'fin': final_string})


def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def view_hist(request):
    current_id = request.user
    context = {
            'past_calcs': Calculation.objects.filter(user=current_id)
            }
    return render(request, 'history.html', context)


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
