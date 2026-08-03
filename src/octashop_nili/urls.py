from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


admin_urls = [
    path('api/admin/catalogs/', include(('apps.catalogs.urls.admin','apps.catalogs'), namespace='catalogs-admin')),
]
front_urls = [
    path('api/front/catalogs/', include(('apps.catalogs.urls.front','apps.catalogs'), namespace='catalogs-front')),
]

doc_urls = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
] + admin_urls + front_urls + doc_urls



admin.site.site_title = "OctaShop - NiliTeb"
admin.site.site_header = "OctaShop - NiliTeb"
admin.site.index_title = "OctaShop - NiliTeb"