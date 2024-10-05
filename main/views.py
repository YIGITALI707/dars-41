from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Players,Nationality
from .serializer import CategorySerializer,NationlitySerializer,PlayersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationlitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

