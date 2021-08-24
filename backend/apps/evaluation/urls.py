from django.urls import path
from rest_framework import routers

from .viewSets.anualEvaluationViewSet import AnualEvaluationViewSet
from .viewSets.monthlyMeliaEvaluationViewSet import MonthlyMeliaEvaluationViewSet
from .viewSets.monthlyGastronomyEvaluationViewSet import MonthlyGastronomyEvaluationViewSet
from . import views

router = routers.DefaultRouter()
router.register('evaluations/anual', AnualEvaluationViewSet)
router.register('evaluations/monthly/melia', MonthlyMeliaEvaluationViewSet)
router.register('evaluations/monthly/gastronomy', MonthlyGastronomyEvaluationViewSet)

urlpatterns = [
    path('evaluations/monthly/melia/resume/', views.getMonthlyPerformanceEvaluationReport)
]
