from rest_framework import routers
from .viewSets import CurrencyViewSet

router = routers.DefaultRouter()
router.register('currency', CurrencyViewSet)
