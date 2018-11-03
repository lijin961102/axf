from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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

    # 商品部分
    shopList = Shop.objects.all()
    shophead = shopList[0]
    shoptab = shopList[1:3]
    shopclass = shopList[3:7]
    shopcommend = shopList[7:11]

    # 商品主体内容
    mainshows = MainShow.objects.all()

    data  ={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainshows':mainshows,
    }

    return render(request,'home/home.html',context=data)

# 闪购超市
def market(request,categoryid):
    # 分类信息
    foodtypes = Foodtypes.objects.all()


    # 分类 点击 下标 >> 分类ID
    typeIndex = int(request.COOKIES.get('typeIndex',0))
    # 根据分类下标 获取 对应 分类ID
    categoryid = foodtypes[typeIndex].typeid
    # 商品信息
    # goodsList = Goods.objects.all()[0:5]
    goodsList = Goods.objects.filter(categoryid=categoryid)

    # 子类信息
    childtupename = foodtypes.get(typeid=categoryid).childtypenames

    # 将每个子类拆分出来
    childTypelist = []
    for item in childtupename.split("#"):
        arr = item.split(':')
        dir = {
            'childname':arr[0], # 子类名称
            'childid':arr[1]    # 子类ID
        }
        childTypelist.append(dir)

    data = {
        'foodtypes':foodtypes, # 分类信息
        'goodsList':goodsList, # 商品信息
        'childTypelist':childTypelist, # 子类信息
    }
    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')


