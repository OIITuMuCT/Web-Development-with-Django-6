
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def view(request):
    return render(request, "base.html", {"message": "Hello World!"})

@login_required
def profile(request):
    return render(request, "profile.html")
