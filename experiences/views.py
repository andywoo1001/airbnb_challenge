from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .serializers import PerkSerializer
from .models import Perk

# Create your views here.


class Perks(APIView):

    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serializer.errors)


class PerkDetail(APIView):

    def get_object(slef, pk):
        try:
            return Perk.Objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serialzier = PerkSerializer(perk)
        return Response(serialzier.data)

    def put(self, request, pk):
        perk = self.get_object(pk)
        serialzier = PerkSerializer(perk, data=request.data, partial=True)
        if serialzier.is_valid():
            updated_perk = serialzier.save()
            return Response(
                PerkSerializer(updated_perk).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete
        return Response(sstatus=HTTP_204_NO_CONTENT)
