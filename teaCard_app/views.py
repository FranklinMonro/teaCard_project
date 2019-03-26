from django.shortcuts import render
from .forms import OperationModelForm, UserLoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "teaCardapp/home.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def tea_card_view(request):

    return render(request, "teaCardapp/teaCard.html")

def data_entry(request):
    return render(request, "teaCardapp/data_entry.html")


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username =  username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failded")
            print("Username:{} and password: {}".format(username, password))
            return HttpResponse("invalid login dtails supplied!")
    else:
        return render(request, 'teaCardApp/login.html',{})

def addData(request):
    dataAdd = False

    if request.method == 'POST':
        enter_job = OperationModelForm(data = request.POST)
        if enter_job.is_valid():
            job = enter_job.save()
            job.save()

        dataAdd = True
        else:
            print(enter_job.errors)

    else:
        enter_job = OperationModelForm()

    return render(request, 'teaCardApp/data_entry.html', {'data_entry':enter_job})
