
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods, GoodsCategory  #这个点的意思是搜索当前目录，也就是goods目录下的所有models
from .filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer #serializer的意思是序列化


class GoodsPagination(PageNumberPagination):
    page_size = 10             #每页多少个。这个类的作用是可以自定义分页，很灵活，有了这个就可以不需要在settings中配置PAGE_SIZE了。
    page_size_query_param = 'page_size'
    page_query_param = "p"     #这里决定了分页中uri显示的的分页名称
    max_page_size = 100        #单页最大数量



class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    #商品列表页，分页，搜索，过滤，排序
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)    #意思是过滤后台设置。所以的过滤方法都需要先在这里引入，然后在下面开始设置如何过滤
    filter_class = GoodsFilter                                       #这个是配置drf页面的过滤功能，这个是过滤商品类
    search_fields = ('name', 'goods_brief', 'goods_desc')            #这个是配置drf的模糊搜索过滤
    ordering_fields = ('sold_num', 'add_time')                       #这个是配置drf的排序功能


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    #List:商品分类列表数据
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


























