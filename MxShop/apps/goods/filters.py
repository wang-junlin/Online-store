import django_filters
from .models import Goods



class GoodsFilter(django_filters.rest_framework.FilterSet):
    #商品的过滤类
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')  #过滤商品价格的最小值，下面那个是最大值；后面的gte就是指定这句代码的功能
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')  #这个参数里的name在django2.0版本之后改为了field_name

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']