from rest_framework import serializers
from .models import Temphum

class TemphumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temphum
        fields = ('id', 'type', 'value', 'latitud', 'longitud', 'tipo_Terreno')