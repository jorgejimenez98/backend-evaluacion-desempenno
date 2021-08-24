from rest_framework import serializers
from .models import Family


class FamilyMiniSerializer(serializers.ModelSerializer):
    desc_grupo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Family
        fields = ['id_grupo', 'desc_grupo']
    
    def get_desc_grupo(self, obj):
        return obj.desc_grupo.rstrip()


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
