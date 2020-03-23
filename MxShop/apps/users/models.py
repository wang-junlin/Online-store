from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser       #contrib是django的一个工具集，里面包含很多东西，比如验证相关的auth，后台相关的xadmin等等。

class UserProfile(AbstractUser):
    #用户
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="famale", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    #短信验证码

    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        #呈现出在xadmin后台中的名称大类，比如商品类，短信验证码类。
        verbose_name = "短信验证码"              #详细名称
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

