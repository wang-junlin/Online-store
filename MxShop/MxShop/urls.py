"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset

router = DefaultRouter()                                 #给DefaultRouter方法创建一个对象，后期的url都会基于routers来配置

router.register(r'goods', GoodsListViewSet, base_name="goods")                  #配置goods的url
router.register(r'codes', SmsCodeViewset, base_name="codes")                    #配置注册页面
router.register(r'categorys', CategoryViewset, base_name="categorys")           #配置category的url
router.register(r'users', UserViewset, base_name="users")                       #用户验证页面
router.register(r'userfavs', UserFavViewset, base_name="userfavs")  #用户对于商品的收藏功能



#源文件中这里有一句from django.contrib import admin
urlpatterns = [
        url(r'^xadmin/', xadmin.site.urls),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #这个是drf登录的一个配置,如果不配置就不会出现登录这个按钮
        url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

        url(r'^', include(router.urls)),         #商品返回到rest framework中的一个列表，这个url的配置在上面22-25行。

        url(r'^docs/', include_docs_urls(title="在线电商")),            #drf自带的文档功能，可以自动生成文档，很方便
        url(r'^api-token-auth/', views.obtain_auth_token),              #drf自带的认证模式
        url(r'^login/', obtain_jwt_token),                              #jwt的认证接口
]
