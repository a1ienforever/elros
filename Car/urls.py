from django.urls import path, include
from rest_framework import routers

from Car.views import *


router = routers.SimpleRouter()
router.register(r"cars", CarApiViewSet)
router.register(r"country", CountryApiViewSet)
router.register(r"manufacturer", ManufacturerApiViewSet)
router.register(r"comment", CommentApiViewSet)

urlpatterns = [
    path("", include(router.urls), name="router"),

]
