from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'description', 'shop', 'location',
            'price', 'discount', 'category', 'stock', 'is_available',
            'picture', '_links',
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than or equal to 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must be greater than or equal to 0.")
        return value

    def get__links(self, obj):
        request = self.context.get('request')
        product_id = str(obj.id)

        return [
            {
                "rel": "self",
                "href": reverse('product-list-create', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', args=[product_id], request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', args=[product_id], request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', args=[product_id], request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]