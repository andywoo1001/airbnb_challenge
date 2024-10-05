from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer

# from django.shortcuts import render
from .models import Category

# Create your views here.


@api_view()
def categories(request):
    all_categoreis = Category.objects.all()
    serializer = CategorySerializer(all_categoreis, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
