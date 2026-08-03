from rest_framework import viewsets
from apps.catalogs.models import Category
from apps.catalogs.serializers.admin import CategoryTreeSerializer, CreateCategoryNodeSerializer, CategoryNodeSerializer, CategoryModificationSerializer
from rest_framework.exceptions import NotAcceptable


class CategoryViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.all().filter(depth = 1)
        else:
            return Category.objects.all()
        
    
    
    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            
            case 'create':
                return CreateCategoryNodeSerializer
            
            case 'retrieve':
                
                return CategoryNodeSerializer
            
            case 'update':
                return CategoryModificationSerializer
            
            case 'partial_update':
                return CategoryModificationSerializer
            case 'destroy':
                return CategoryModificationSerializer

            case _:
                raise NotAcceptable()
            
        