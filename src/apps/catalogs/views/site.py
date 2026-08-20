from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from apps.catalogs.infrastructure.models import LastOffer, Product
from apps.catalogs.serializers.site import LastOfferSerializer, ProductLastOfferSerializer, ProductSerializer

# ReadOnlyModelViewSet:
# methods:{ get.all , get.by_id}
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_public = True)
    serializer_class = ProductSerializer
    def get_queryset(self):
        filter_query = Q()
        products_title = self.request.query_params.get('q')
        if products_title is not None:
            products_title = products_title.replace("/","")
            filter_query = Q(product_name__icontains=products_title)
        queryset = self.queryset.filter(filter_query)
        return queryset
    
class ProductLastOfferApiView(viewsets.ReadOnlyModelViewSet):
    queryset = LastOffer.objects.all()
    serializer_class = ProductLastOfferSerializer
    
    def get(self, request, format=None):
        serializer = ProductLastOfferSerializer(self.queryset, context={"request": 
                      request}, many=True)
        return Response(serializer.data) 
    
    
class LastOfferAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(stockrecords__in_offer=True,is_public=True)
        serializer = LastOfferSerializer(products, many=True, context={"request": 
                      request})
        return Response(serializer.data)