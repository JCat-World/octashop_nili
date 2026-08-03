from rest_framework import viewsets
from apps.catalogs.infrastructure.models import Category
from apps.catalogs.serializers.front import CategorySerializer




class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer