from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField   #引入外置app

class GoodsCategory(models.Model):
    #商品类别
    CATEGORY_TYPE = (
        (1,"一级类别"),
        (2,"二级类别"),
        (3,"三级类别"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")          #编码，可通过字母英文来搜索
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")                         #简单描述
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")  #整数，选择1、2、3级类;category的意思是类别类型
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat") #parent_actegory的意思是父类别；创建外键，这句代码是为了从父类别中选择级别
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")                  #将商品类别中的tab放入选择首页tab栏
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name   #详细名称复用

    def __str__(self): #在页面中返回创建的名称，应该是在admin中看，不设置这个的话admin中的名字就会直接显示默认的名字
        return self.name



class GoodsCategoryBrand(models.Model):
    #商品品牌类别；品牌名。主页推荐的商家图片中把鼠标放上去会显示出名字。

    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name="商品类目") #引入上面的商品类别的类
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/") #设置品牌图片的保存位置，源码中此处应该是 image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间") #添加时的初始日期时间

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    #商品详情和主页一部分商品画面（比如主页推荐的商品等等）

    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
    #继承商品类别，默认是必须选择一个（默认为null = False），不能为空，如果手动加（null = Ture），那么就可以不选类别。

    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号") #商品编码
    name = models.CharField(max_length=300, verbose_name="商品名")                      #名称
    click_num = models.IntegerField(default=0, verbose_name="点击数")                   #点击数
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")                #出售数量
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")                     #收藏数量
    goods_num = models.IntegerField(default=0, verbose_name="库存数")                   #商品库存数量
    market_price = models.FloatField(default=0, verbose_name="市场价格")                #市场价格
    shop_price = models.FloatField(default=0, verbose_name="本店价格")                  #商店价格
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")         #商品简介，简介可能比较长所以用TextField
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300)
    #富文本编辑器，用这个可以在后台编辑商品的描述;在后台用富文本编辑的时候，imagepath可以单独设置图片的保存位置；filepath可以设置文件的保存位置

    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")           #用布尔运算来确定某件商品是否免配送费；设置为default为Ture，应该就是选择是否承担运费
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图") #意思是商品正面形象，就是主页中推荐的商品
    is_new = models.BooleanField(default=False, verbose_name="是否新品")                 #用布尔运算来确定主页中商品新品的商品是哪个
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")                 #用布尔运算来确定热卖商品是哪个

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="商品类目")
    goods = models.ForeignKey(Goods, related_name='goods')

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    #商品轮播图

    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)         #轮播图存放位置
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url") #图片url
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
        #在这个类中使用上面Goods类中的name，所以要在这个类中的goods中继承上面的Goods类。


class Banner(models.Model):
    #轮播的商品

    goods = models.ForeignKey(Goods, verbose_name="商品") #使用外键，键Goods这个类，也就是商品类；因为要点击banner中的图就能跳入该商品详情页去。
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    #这个是单独显示的轮播大图片，不能为空，默认就是null=false，所以就不用管它；upload_to="banber"，图片存放目录，会自动在之前创建的media中放入此图片。

    index = models.IntegerField(default=0, verbose_name="轮播顺序") #在后台中管理轮播图的顺序
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    #热搜词

    keywords = models.CharField(max_length=20, default="", verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


