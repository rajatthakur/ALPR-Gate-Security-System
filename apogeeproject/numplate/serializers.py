from rest_framework import serializers
from .models import CarPlate

class CarPlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPlate
        fields = "__all__"