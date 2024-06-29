# reports/serializers.py

from rest_framework import serializers
from .models import CrimeReport

class CrimeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeReport
        fields = '__all__'
