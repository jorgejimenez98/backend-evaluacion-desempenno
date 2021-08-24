from rest_framework import routers
from .viewSet import PuntoDeVentaViewSet

router = routers.DefaultRouter()
router.register('puntoDeVentas', PuntoDeVentaViewSet)
