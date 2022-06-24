from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("organizations", OrganizationViewSet)
router.register("images", ImagesViewSet)
router.register("settings", SettingsViewSet)
# router.register("orders", OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]
