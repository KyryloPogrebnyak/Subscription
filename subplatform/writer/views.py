from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_view')
def writer_dashboard(request):
    return render(request, 'writer/writer-dashboard.html')