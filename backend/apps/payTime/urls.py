from rest_framework import routers
from .viewsets import PayTimeViewSet

router = routers.DefaultRouter()
router.register('payTimes', PayTimeViewSet)
