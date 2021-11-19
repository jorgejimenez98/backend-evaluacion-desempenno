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
from ..hotel.models import Hotel
from ..payTime.models import PayTime
from ..payTime.serializers import PayTimeSerializer
from .helpFunctions import buildEval, selection_sort


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
        # Get last 3 Paytimes
        paytimes = list(PayTime.objects.filter(
            isEliminated=False).order_by('-year', '-monthOrder')[0:3])

        # Validate if There is Paytimes
        if len(paytimes) == 0:
            return Response([], status=status.HTTP_200_OK)

        # Build Response
        listToReturn = []
        for hotel in Hotel.objects.all():
            for worker in hotel.workers.filter(activo=True):
                # BuildEvals
                firstEval = buildEval(1, 0, paytimes, worker)
                secondEval = buildEval(2, 1, paytimes, worker)
                thirdEval = buildEval(3, 2, paytimes, worker)

                # Append new data to list to return
                listToReturn.append({
                    # Worker Data
                    "name": worker.nombreCompleto(),
                    "hotel": hotel.name,
                    # First Eval
                    "firstEvalDate": firstEval['payTimeName'] if firstEval is not None else None,
                    "firstEvalCalification": firstEval['totalCalificacion'] if firstEval is not None else None,
                    "firstEvalTotal": firstEval['totalPoints'] if firstEval is not None else None,
                    "firstcalificacion": firstEval['calificacion'] if firstEval is not None else "No Registrada",
                    # Second Eval
                    "secondEvalDate": secondEval['payTimeName'] if secondEval is not None else None,
                    "secondEvalCalification": secondEval['totalCalificacion'] if secondEval is not None else None,
                    "secondEvalTotal": secondEval['totalPoints'] if secondEval is not None else None,
                    "secondcalificacion": secondEval['calificacion'] if secondEval is not None else "No Registrada",
                    # Second Eval
                    "thirdEvalDate": thirdEval['payTimeName'] if thirdEval is not None else None,
                    "thirdEvalCalification": thirdEval['totalCalificacion'] if thirdEval is not None else None,
                    "thirdEvalTotal": thirdEval['totalPoints'] if thirdEval is not None else None,
                    "thirdcalificacion": thirdEval['calificacion'] if thirdEval is not None else "No Registrada",
                })

        # Sort Response
        listToOrder = [i for i in listToReturn if i['firstEvalTotal'] is not None]
        listNotOrder = [i for i in listToReturn if i['firstEvalTotal'] is None]
        selection_sort(listToOrder)
        # Return Response
        listToReturn = listToOrder + listNotOrder
        return Response(listToReturn, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
