from django.shortcuts import render
from rest_framework import generics
from .serializers import ProviderSerializer
from .models import Provider


class ProviderList(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
