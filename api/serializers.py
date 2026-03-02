from api.models import Insurance
from rest_framework import serializers



class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Insurance
        fields='__all__'