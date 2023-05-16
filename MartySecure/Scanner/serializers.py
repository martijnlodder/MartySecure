from rest_framework import serializers
from .models import ValidatedResult


# Python-objecten om zetten naar JSON en omgekeerd
class ValidatedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidatedResult
        fields = ['port', 'service', 'version',
                  'vulnerability', 'description', 'severity']
