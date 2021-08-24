from rest_framework import routers
from .viewsets import OccupationalCategoryViewSet

router = routers.DefaultRouter()
router.register('ocuppationalCategories', OccupationalCategoryViewSet)