from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..salesPlan.models import MonthlySalePlan
from ..family.models import Family
from ..sellArea.models import PuntoDeVenta
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMainNumbers(request):
    try:
        response = {
            'users': User.objects.all().count(),
            'salePlans': MonthlySalePlan.objects.all().count(),
            'families': Family.objects.filter(activo=True).count(),
            'salePlaces': PuntoDeVenta.objects.filter(activo=True).count(),
        }
        return Response({'data', json.dumps(response)}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
