from django.shortcuts import render

from .serializers import (
    ReceitaIngredienteSerializer
)
from .models import ReceitaIngrediente

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateIngrediente(APIView):
    serializer_class = ReceitaIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListIngrediente(APIView):
    serializer_class = ReceitaIngredienteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(ReceitaIngrediente.objects.all(), many=True)
        return Response(serializer.data)

class EditIngrediente(APIView):
    serializer_class = ReceitaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(ReceitaIngrediente.objects.get(id_receita_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(ReceitaIngrediente.objects.get(id_receita_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteIngrediente(APIView):
    serializer_class = ReceitaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(ReceitaIngrediente.objects.get(id_receita_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        ReceitaIngrediente.objects.get(id_receita_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
