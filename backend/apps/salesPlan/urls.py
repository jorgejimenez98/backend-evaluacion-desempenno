from rest_framework import routers
from .viewsets import AnualSalePlanViewSet

router = routers.DefaultRouter()
router.register('salePlans/anual', AnualSalePlanViewSet)