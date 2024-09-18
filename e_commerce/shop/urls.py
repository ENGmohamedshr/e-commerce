

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views

router =  DefaultRouter()
router.register(r'category',views.CategoryAPI ,basename='category')
router.register(r'product',views.ProductAPI,basename='product')

urlpatterns= router.urls
    
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)