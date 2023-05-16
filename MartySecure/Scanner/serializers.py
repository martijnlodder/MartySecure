from rest_framework import serializers
from .models import ValidatedResult

class ValidatedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidatedResult
        fields = ['port', 'service', 'version', 'vulnerability', 'description', 'severity']
