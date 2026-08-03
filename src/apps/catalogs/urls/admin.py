from rest_framework.routers import SimpleRouter

from apps.catalogs.views.admin import CategoryViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet, basename='category')
urlpatterns = [] + router.urls