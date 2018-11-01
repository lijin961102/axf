from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy


def base(request):
    return render(request,'base/base.html')

# 首页
def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    # 导航数据
    navs = Nav.objects.all()

    # 每日必购
    mustbuys = Mustbuy.objects.all()

    data  ={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
    }

    return render(request,'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')


