from rest_framework import serializers
from .models import AnualSalePlan, MonthlySalePlan
from ..hotel.serializers import HotelMiniSerializer


class MonthlySalePlanForEditSerializer(serializers.ModelSerializer):
    family = serializers.SerializerMethodField(read_only=True)
    saleArea = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MonthlySalePlan
        fields = ['id', 'month', 'plan', 'family', 'saleArea']

    def get_saleArea(self, obj):
        return obj.saleArea.id_pvta

    def get_family(selr, obj):
        return obj.family.id_grupo


class MonthlySalePlanSerializer(serializers.ModelSerializer):
    family = serializers.SerializerMethodField(read_only=True)
    saleArea = serializers.SerializerMethodField(read_only=True)
    coinAcronimun = serializers.SerializerMethodField(read_only=True)
    hotelId = serializers.SerializerMethodField(read_only=True)
    monthOrder = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MonthlySalePlan
        fields = ['id', 'month', 'plan', 'family', 'saleArea',
                  'coinAcronimun', 'anualSalePlan', 'hotelId', 'monthOrder']

    def get_saleArea(self, obj):
        return obj.saleArea.desc_pvta.rstrip()

    def get_family(selr, obj):
        return obj.family.desc_grupo.rstrip()

    def get_coinAcronimun(self, obj):
        return obj.anualSalePlan.currency.acronym.rstrip()

    def get_hotelId(self, obj):
        return obj.anualSalePlan.hotel.pk

    def get_monthOrder(self, obj):
        monthList = 'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'.split()
        months = {i[1]: i[0] + 1 for i in enumerate(monthList)}
        return months[obj.month]


class AnualSalePlanMiniSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField(read_only=True)
    currency = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AnualSalePlan
        fields = ['id', 'hotel', 'year', 'currency']

    def get_hotel(self, obj):
        return HotelMiniSerializer(obj.hotel, many=False).data

    def get_currency(self, obj):
        return f'{obj.currency.description.rstrip()}({obj.currency.acronym.rstrip()})'


class AnualSalePlanSerializer(AnualSalePlanMiniSerializer):
    monthlySalePlans = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AnualSalePlan
        fields = ['id', 'hotel', 'year', 'currency', 'monthlySalePlans']

    def get_monthlySalePlans(self, obj):
        return MonthlySalePlanSerializer(obj.monthlySalePlans.all().order_by('-pk'), many=True).data
