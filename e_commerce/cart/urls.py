from rest_framework.routers import DefaultRouter

from .views import CartAPI


router= DefaultRouter()
router.register(r'',CartAPI , basename='cart')

urlpatterns = router.urls