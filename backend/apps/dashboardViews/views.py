from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from backend.extraPermissions import IsFoodAndDrinkBoss
from ..evaluation.models import MonthlyMeliaEvaluation, AnualEvaluation
from ..salesPlan.models import MonthlySalePlan
from ..family.models import Family
from ..sellArea.models import PuntoDeVenta


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
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRangeOfMelyaEvaluations(request):
    try:
        response = {'veryGood': 0, 'good': 0, 'regular': 0, 'bad': 0}
        for evaluation in MonthlyMeliaEvaluation.objects.all():
            if evaluation.totalCalificacion().split('-')[1].lstrip() == 'MB':
                response['veryGood'] += 1
            elif evaluation.totalCalificacion().split('-')[1].lstrip() == 'B':
                response['good'] += 1
            elif evaluation.totalCalificacion().split('-')[1].lstrip() == 'R':
                response['regular'] += 1
            elif evaluation.totalCalificacion().split('-')[1].lstrip() == 'M':
                response['bad'] += 1
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRangeOfAnualEvaluations(request):
    try:
        response = {'veryGood': 0, 'good': 0, 'bad': 0}
        for evaluation in AnualEvaluation.objects.all():
            if evaluation.finalEvaluation == 'Superior':
                response['veryGood'] += 1
            elif evaluation.finalEvaluation == 'Adecuado':
                response['good'] += 1
            elif evaluation.finalEvaluation == 'Deficiente':
                response['bad'] += 1
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsFoodAndDrinkBoss])
def getTableEvaluations(request):
    try:
        message = "All is ok"
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
