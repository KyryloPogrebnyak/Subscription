from django.shortcuts import render
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def home(request):
    return render(request, "account/index.html")


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()

            return HttpResponse("User created successfully!")
        
    context = {"RegisterForm": form}

    return render(request, "account/register.html", context)


def login_view(request):

    form = AuthenticationForm()
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_writer == True:
                login(request, user)
                return redirect("writer-dashboard")
            
            if user is not None and user.is_writer == False:
                login(request, user)
                return redirect("client-dashboard")
    
    context = {"LoginForm": form}

    return render(request, "account/login.html", context)
