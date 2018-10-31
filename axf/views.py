from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base/base.html')

def index(request):
    return None


def home(request):

    return render(request,'home/home.html')


def market(request):
    return None


def cart(request):
    return None


def mine(request):
    return None


