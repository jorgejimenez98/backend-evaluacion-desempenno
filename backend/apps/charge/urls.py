from rest_framework import routers
from .viewsets import ChargeViewSet

router = routers.DefaultRouter()
router.register('charges', ChargeViewSet)
