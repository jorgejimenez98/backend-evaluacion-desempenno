from rest_framework import routers
from .viewSet import WorkerViewSet

router = routers.DefaultRouter()
router.register('workers', WorkerViewSet)
