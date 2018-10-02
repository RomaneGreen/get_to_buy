from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login(request):
    return render(request,'home.html',{})

def logout(request):
    return render(request,'home.html',{})

def home(request):
    return render(request,'home.html',{})

def gig_detail(request, id):
    return render(request,'gig_detail.html',{})
