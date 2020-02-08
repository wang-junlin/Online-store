from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )    #此代码作用：在点击收藏商品时，自动收藏到当前登录的用户中去

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")