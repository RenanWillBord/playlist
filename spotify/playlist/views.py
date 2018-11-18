from django.shortcuts import render

from rest_framework import generics
from .models import PlayList
from .serializers import PlayListSerializer

from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PlayListList(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer


class PlayListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
