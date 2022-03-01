from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from phones.views import PhoneViewSet

router = DefaultRouter()
router.register('phones', PhoneViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]

