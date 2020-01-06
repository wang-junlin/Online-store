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

from goods.views import GoodsListViewSet, CategoryViewset
router = DefaultRouter()                                             #给DefaultRouter方法创建一个对象，后期的url都会基于routers来配置

router.register(r'goods', GoodsListViewSet, base_name="goods")         #配置goods的url
router.register(r'category', CategoryViewset, base_name="categorys")      #配置category的url

#源文件中这里有一句from django.contrib import admin
urlpatterns = [
        url(r'^xadmin/', xadmin.site.urls),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #这个是drf登录的一个配置,如果不配置就不会出现登录这个按钮
        url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

        url(r'^', include(router.urls)),  #商品返回到rest framework中的一个列表，这个url的配置在上面22-25行。

        url(r'^docs/', include_docs_urls(title="慕学生鲜")),
]
