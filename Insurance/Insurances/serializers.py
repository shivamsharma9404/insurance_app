from rest_framework import serializers
from .models import Insurance,Transacts
from django.db import models
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacts
        fields = '__all__'

class InsuranceSerializers(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True, required=False)
    class Meta :
        model = Insurance
        fields ="__all__"
