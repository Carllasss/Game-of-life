from .models import Cells
from rest_framework import serializers


class CellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cells
        fields = '__all__'
