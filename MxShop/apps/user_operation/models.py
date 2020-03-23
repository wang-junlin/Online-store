from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
User = get_user_model()

class UserFav(models.Model):
    #用户收藏

    user = models.ForeignKey(User, verbose_name="用户") #从上面引入的user中使用User这个外键
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id") #也是一样从goodsAPP的模型中引入Goods
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods") #此代码作用：让用户对同一件商品只能收藏一次，不能重复。

    def __str__(self):
        return self.user.username
        #是引用的usersmodels中的name

class UserLeavingMessage(models.Model):
    #用户留言

    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )

    user = models.ForeignKey(User, verbose_name="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型: 1(留言), 2(投诉), 3(询问), 4(售后), 5(求购)")
    #用户留言前要选择的类型，比如投诉、售后等。不要直接用type，因为是关键词。直接在前面设置好类型中的选项，然后在这里引用就可以了.u表示后面的是utf-8的字符串，避免报错。

    subject = models.CharField(max_length=100, default="", verbose_name="主题")             #留言的主题
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")    #留言的内容
    file = models.FileField(verbose_name="上传的文件", help_text="上传的文件")               #上传的文件，图片之类
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
        #要返回subject，也就是主题，这样在后台中便于观看，可以直接看见主题的名字。


class UserAddress(models.Model):
    #用户收货地址

    user = models.ForeignKey(User, verbose_name="用户")
    district = models.CharField(max_length=100, default="", verbose_name="区域")      #区域
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")   #收货地址
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人") #签收人姓名
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")  #签收人电话
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address









