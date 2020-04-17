from rest_framework.routers import DefaultRouter
from .views import ProductListViewSet, CategoryListViewSet


router = DefaultRouter()


router.register(r'products',ProductListViewSet, basename='products')
router.register(r'categories',CategoryListViewSet, basename='categories')
# router.register(r'categories/<int:pk>', ProductListViewSet, basename='category-products')


urlpatterns = router.urls

