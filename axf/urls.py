from django.conf.urls import url

from axf import views
app_name = 'axf'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^base/$',views.base,name='base'),
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='market'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),
]