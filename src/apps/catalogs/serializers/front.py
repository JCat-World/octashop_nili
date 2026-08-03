from rest_framework import serializers
from apps.catalogs.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'name', 'slug', 'parent', 'image', 'description']
        fields = '__all__'