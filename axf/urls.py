from django.conf.urls import url

from axf import views
app_name = 'axf'

urlpatterns = [
    url(r'^$',views.home,name='home'), # 首页
    url(r'^market/(\d+)/$',views.market,name='market'), # 闪购超市
    url(r'^cart/$',views.cart,name='cart'), # 购物车
    url(r'^mine/$',views.mine,name='mine'), # 我的

    url(r'^registe/$',views.registe,name='registe'),
]