from django.shortcuts import render

from .serializers import (
    CreateIngredienteSerializer,
    ListIngredienteSerializer,
    DetailsIngredienteSerializer
)
from .models import Ingrediente

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateIngrediente(APIView):
    serializer_class = CreateIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListIngrediente(APIView):
    serializer_class = ListIngredienteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Ingrediente.objects.all(), many=True)
        return Response(serializer.data)

class DetailsIngrediente(APIView):
    serializer_class = DetailsIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Ingrediente.objects.get(id_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
