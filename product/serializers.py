from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'

    # def to_representation(self, obj):
    #     lst = []
    #     for img in list(obj):
    #         url = img[1]
    #         request = self.context.get('request', None)
    #         # print(request.build_absolute_uri())
    #         if request is not None:
    #             # print(url)
    #             image = request.build_absolute_uri(url)
    #             # print(image)
    #             lst.append(image)
    #
    #     return lst
    #


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

    def to_representation(self, obj):
        serializer = ImagesSerializer(obj.images, many=True)
        datas = serializer.data
        lst = []
        for data in datas:
            url = data['image']
            request = self.context.get('request', None)
            if request is not None:
                url = request.build_absolute_uri(url)
                lst.append(url)

        return {
            "id": obj.id,
            "name": obj.name,
            "info": obj.info,
            "images": lst,
            "price": obj.price,
            "created": obj.created,
            "material": obj.material,
            "color": obj.color,
            "category": {
                "name": obj.category.name,
                "id": obj.category.id
            } if obj.category else None,
            "organization": {
                "name": obj.organization.name,
                "id": obj.organization.id
            } if obj.organization else None
        }


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # def to_representation(self, obj):
    #     if not obj:
    #         return None
    #     return {
    #         "id": obj.id,
    #         "total": obj.total,
    #         "phone": obj.phone,
    #         "address": obj.address,
    #         "created": obj.created,
    #         "bottle": {
    #             "name_uz": obj.bottle.name_uz,
    #             "name_en": obj.bottle.name_en,
    #             "name_ru": obj.bottle.name_ru,
    #             "id": obj.bottle.id
    #          }
    #     }
