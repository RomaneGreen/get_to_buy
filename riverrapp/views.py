from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Gig, Profile, Purchase, Review
from .forms import GigForm
import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,merchant_id="8wxwtqfdxqrcy6v9",public_key="st9rt59t4hfjk2dz",private_key="b8eb2e84d4e9892aa2533d7d1878bb1")

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

    review = Review.objects.filter(gig=gig)
    client_token = braintree.ClientToken.generate()
    return render(request,'gig_detail.html',{"review":review,"gig":gig,"client_token":client_token})

@login_required(login_url="/")
def create_gig(request):
    error = ''
    if request.method == 'POST':
        gig_form = GigForm(request.POST,request.FILES)
        if gig_form.is_valid():
           gig = gig_form.save(commit=False)
           gig.user = request.user
           gig.save()
           return redirect('my_gigs')
        else:
            error = 'Data is not valid'
        print(gig_form.is_valid())
        print(gig_form.errors())
    gig_form = GigForm()
    return render(request,'create_gig.html',{"error":error})

@login_required(login_url="/")
def edit_gig(request,id):
    try:
        gig = Gig.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            gig_form = GigForm(request.POST,request.FILES,instance=gig)
            if gig_form.is_valid():
                gig.save()
                return redirect('my_gigs')
            else:
                error = 'Data is not valid'
        return render(request,'edit_gig.html',{"gig":gig,"error": error})
    except Gig.DoesNotExist:
        return redirect('/')



@login_required(login_url="/")
def my_gigs(request):
    gigs = Gig.objects.filter(user = request.user)
    return render(request,'my_gigs.html',{"gigs":gigs})

@login_required(login_url="/")
def profile(request,username):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.about = request.POST['about']
        profile.slogan = request.POST['slogan']
        profile.save()
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
           return redirect("/")
    gigs = Gig.objects.filter(user = profile.user,status=True)
    return render(request,'profile.html',{"profile":profile,"gigs":gigs})

@login_required(login_url="/")
def create_purchase(request):
    if request.method == 'POST':
        try:
            gig = Gig.objects.get(id = request.POST['gig_id'])
        except Gig.DoesNotExist:
            return redirect("/")

        nonce = request.POST["payment_method_nonce"]
        result = braintree.Transaction.sale({
            "amount": gig.price,
            "payment_method_nonce": nonce

        })

        if result.is_success:
            # Purchase.objects.create(gig=gig, buyer=request.user)
            print("Buy gig success!")
        else:
            print("Buy gig failed!")
    return redirect('/')

@login_required(login_url="/")
def my_sellings(request):
    purchases = Purchase.objects.filter(gig__user=request.user)
    return render(request,'my_sellings.html',{"purchases":purchases})

@login_required(login_url="/")
def my_buyings(request):
    purchases = Purchase.objects.filter(buyer=request.user)
    return render(request,'my_buyings.html',{"purchases":purchases})
