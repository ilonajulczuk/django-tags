from rest_framework.routers import DefaultRouter

from .views import LibraryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'libraries', LibraryViewSet)
router.register(r'tags',TagViewSet)
urlpatterns = router.urls
