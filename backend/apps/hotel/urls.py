from rest_framework import routers
from django.urls import path
from . import viewSet as views

router = routers.DefaultRouter()
router.register('hotels', views.HotelViewSet)

urlpatterns = [
    path('hotels/allow/<int:pk>/', views.getHotelWithOutPermission, name='getHotelWithOutPermission'),
    path('hotels/allow/', views.getHotelsWithOutPermission, name='getHotelsWithOutPermission'),
]
