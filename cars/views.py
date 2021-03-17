from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

