from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login_view")
def client_dashboard(request):
    return render(request, "client/client-dashboard.html")
