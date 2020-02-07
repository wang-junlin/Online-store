
import sys
import os

#sys是一个python模块，引入之后可以用这个模块里的方法或者说函数。作用是控制系统方面的东西
#os是一个python模块，作用是控制文件方面的东西

pwd = os.path.dirname(os.path.realpath(__file__))   #os.path.name的作用是返回文件路径，os.path.realpath的作用是返回path的真实路径
sys.path.append(pwd+"../")   #sys.path.append作用是自定义模块路径，把MxShop这个路径加了进去。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings") #指定根目录就是这个项目的目录，后面他就会自动来这个目录下来找这个文件

import django
django.setup()  #不知道这个函数是干嘛的，但setup是安装的意思,或者也是启动的意思

from goods.models import Goods,GoodsCategory,GoodsImage #这句一定要放在14、15这两行的下面，不能放在最顶上。因为必须要先把django引入之后才能写这个，不然会报错
from db_tools.data.product_data import row_data  #引入商品

for goods_detail in row_data:
    #上面的row_data是在produ_data.py这个文件里引入的
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", ""))) #意思是市场价格；这里应该是用replace函数来替换"￥"这个符号。
    goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", ""))) #意思是本店价格；
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""  #前面的goods.brief是在Goods的models中，后面的goods_detail是在product中，这几个需要一一对应
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

    category_name = goods_detail["categorys"][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detail["images"]:
        #轮播图的数据表
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()








