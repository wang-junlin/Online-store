from rest_framework import serializers

from goods.models import Goods, GoodsCategory, HotSearchWords, GoodsImage

class CategorySerializer3(serializers.ModelSerializer):
    #商品第三类别序列化
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    #商品第二类别序列化
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    #商品类别序列化
    sub_cat = CategorySerializer2(many=True)  #many的意思是是否数据为多个，将它等于Ture表示是的。
    class Meta:
        model = GoodsCategory
        fields = "__all__"
        #引入这个类的原因是Goods中引入了Goodscategory这个外键，所以要想在Goods中显示出这个外键的信息就需要引入这个类。

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image", )

class GoodsSerializer(serializers.ModelSerializer):
    #使用ModelSerializer来实现序列化，直接将serializer和model进行映射，在下面直接指定model就可以进行序列化
    category = GoodsCategory()   #这个是将上面的类使用到这个Goods类里面，直接将数据进行覆盖。
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"

