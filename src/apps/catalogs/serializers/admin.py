from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from apps.catalogs.infrastructure.models import Category
from drf_spectacular.utils import extend_schema_field


class CreateCategoryNodeSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False, allow_null=True)
    def create(self, validated_data):
        parent = validated_data.pop('parent', None)
        
        if parent is None:
          instance = Category.add_root(**validated_data)
        else:
          parent_node = get_object_or_404(Category, pk=parent)
          instance = parent_node.add_child(**validated_data)
        return instance
    class Meta:
        model = Category
        fields = ('id','title', 'description', 'is_public', 'slug', 'parent')



class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_public', 'slug', 'children')
    
    def get_children(self, obj):
        return CategoryTreeSerializer(obj.get_children(), many=True).data
      
CategoryTreeSerializer.get_children = extend_schema_field(serializers.ListField(child=CategoryTreeSerializer()))(CategoryTreeSerializer.get_children)


class CategoryNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title', 'description', 'is_public',)
