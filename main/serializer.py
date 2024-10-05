from rest_framework import serializers
from .models import Category,Players,Nationality



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class NationlitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Nationality
        fields='__all__'


class  PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Players
        fields='__all__'
