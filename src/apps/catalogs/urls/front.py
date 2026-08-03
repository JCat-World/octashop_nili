from rest_framework.routers import SimpleRouter

from apps.catalogs.views.front import CategoryViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
urlpatterns = [] + router.urls