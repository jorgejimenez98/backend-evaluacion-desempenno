from rest_framework import routers
from .viewSet import FamilyViewSet

router = routers.DefaultRouter()
router.register('families', FamilyViewSet)
