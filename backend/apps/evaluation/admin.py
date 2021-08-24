from django.contrib import admin
from .models import MonthlyGastronomyEvaluation, MonthlyMeliaEvaluation, AnualEvaluation

admin.site.register(AnualEvaluation)
admin.site.register(MonthlyGastronomyEvaluation)
admin.site.register(MonthlyMeliaEvaluation)
