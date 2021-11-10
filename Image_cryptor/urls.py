from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet,keyGenView,DecryptViewSet

router = routers.DefaultRouter()

router.register(r'upload', UploadViewSet, basename="upload")

router.register(r'key_gen', keyGenView, basename="keyGenView")

router.register(r'decrypt', DecryptViewSet, basename="DecryptView")

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),

]