from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Gig

# Create your views here.
@login_required
def login(request):
    return render(request,'home.html',{})

def logout(request):
    return render(request,'home.html',{})

def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request,'home.html',{"gigs":gigs})

def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id = id)
    except Gig.DoesNotExist:
        return redirect('/')

    return render(request,'gig_detail.html',{"gig":gig})

def create_gig(request):
    return render(request,'create_gig.html',{})

def my_gigs(request):
    return render(request,'my_gigs.html',{})
