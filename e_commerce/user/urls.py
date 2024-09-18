
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import UserAPI

router = DefaultRouter()

router.register(r'',UserAPI , basename='users')

urlpatterns = [
    path('get-token/', views.obtain_auth_token),
   
]
urlpatterns += router.urls