from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods #从该模型中引入类，下面会用到
User = get_user_model()        #给user类赋值

class ShoppingCart(models.Model):
    #购物车
    user = models.ForeignKey(User, verbose_name=u"用户")           #在这里用外键继承前面引入的user类
    goods = models.ForeignKey(Goods, verbose_name=u"商品")          #继承goods。models中的Goods
    nums = models.IntegerField(default=0, verbose_name="购买数量") #购物车商品数量，默认等于0

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        #源代码中这里有一个 unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)

class OrderInfo(models.Model):
    #订单

    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("cancel", "待支付"),
    )


    user = models.ForeignKey(User, verbose_name="用户") #订单要和用户相关联，所以调用users模型里的user
    order_sn = models.CharField(max_length=30, unique=True, verbose_name="订单号") #订单编号,unique=ture就是唯一编号，不能重复。
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号码") #交易订单号，支付宝支付需要使用。
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=30, verbose_name="订单状态") #支付状态，是否支付成功。
    post_script = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")                       #支付金额
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")             #支付时间

    #用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")  #收货地址默认为空
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人") #签收人姓名
    singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")         #签收人电话

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    #订单的商品详情

    order = models.ForeignKey(OrderInfo, verbose_name="订单信息", related_name="goods") #继承订单类
    goods = models.ForeignKey(Goods, verbose_name="商品")                               #继承商品类
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")                 #需定一个默认值

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
        #order.order_sn是用的前面order中的order_sn


