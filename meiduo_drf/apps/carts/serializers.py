# _*_coding : uft-8 _*_
# @Time : 2023/7/3 21:56
# @Author : 
# @File : serializers
# @Project : meiduo_drf
from rest_framework import serializers

from apps.goods.models import SKU


class CartsSerializer(serializers.Serializer):
    """ 购物车 添加/修改 序列化器 """
    sku_id = serializers.IntegerField(label='商品sku_id', min_value=1)
    count = serializers.IntegerField(label='商品数量', min_value=1)
    selected = serializers.BooleanField(label='是否选中', default=True)

    def validate_sku_id(self, value):
        try:
            SKU.objects.get(id=value)
        except SKU.DoesNotExist:
            raise serializers.ValidationError('商品信息不存在')
        return value


class SKUCartsModelSerializer(serializers.ModelSerializer):
    """ 购物车展示序列化器 """
    count = serializers.IntegerField(label='商品数量', min_value=1)
    selected = serializers.BooleanField(label='是否选中')

    class Meta:
        model = SKU
        fields = ['id', 'name', 'price', 'default_image', 'count', 'selected']


class CartDeleteSerializer(serializers.Serializer):
    """ 购物车删除 """
    sku_id = serializers.IntegerField(label='商品sku_id', min_value=1)

    def validate_sku_id(self, value):
        try:
            SKU.objects.get(id=value)
        except SKU.DoesNotExist:
            raise serializers.ValidationError('商品信息不存在')
        return value


class CartSelectedAllSerializer(serializers.Serializer):
    """ 购物车是否全选序列化器 """
    selected = serializers.BooleanField(label='是否全选')
