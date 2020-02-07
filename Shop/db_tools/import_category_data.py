__author__ = 'bobby' #意思是作者为bobby

#接下来是独立使用django的model
import sys
import os

#sys是一个python模块，引入之后可以用这个模块里的方法或者说函数。作用是控制系统方面的东西
#os是一个python模块，作用是控制文件方面的东西

pwd = os.path.dirname(os.path.realpath(__file__))   #os.path.name的作用是返回文件路径，os.path.realpath的作用是返回path的真实路径
sys.path.append(pwd+"../")   #sys.path.append作用是自定义模块路径，把MxShop这个路径加了进去。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings") #指定根目录就是这个项目的目录，后面他就会自动来这个目录下来找这个文件

import django
django.setup()  #不知道这个函数是干嘛的，但setup是安装的意思,或者也是启动的意思

from goods.models import GoodsCategory #这句一定要放在14、15这两行的下面，不能放在最顶上。因为必须要先把django引入之后才能写这个，不然会报错
from db_tools.data.category_data import row_data  #引入商品类别

#all_categorys = GoodsCategory.objects.all()
#objects是Django帮我们自动生成的管理器对象，通过这个管理器可以实现对数据的查询， objects是models.Manager类的一个对象，如果我们模型类中添加一个models.Manger类或者其子类变量，那么Django就不再帮我们生成默认的objects管理器。
#自定义管理器的应用场景：案例： 调用BookInfo.objects.all()返回没有删除的图书的数据

for lev1_cat in row_data:
    #lev的意思是等级
    #下面是一个嵌套循环，用来写后台中商品类别选项中的排列。类别的数据是从category_data.py这个文件中导入进来的。然后我们再用下面的逻辑把他导入进xadmin后台中。

    lev1_intance = GoodsCategory()
    #intance的意思是维护、维持

    lev1_intance.code = lev1_cat["code"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1   #这里的意思是这个等级类目等于1，1在goods.models中。
    lev1_intance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_intance = GoodsCategory()
        lev2_intance.code = lev2_cat["code"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.category_type = 2
        lev2_intance.parent_category = lev1_intance
        lev2_intance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_intance = GoodsCategory()
            lev3_intance.code = lev3_cat["code"]
            lev3_intance.name = lev3_cat["name"]
            lev3_intance.category_type = 3
            lev3_intance.parent_category = lev2_intance
            lev3_intance.save()










