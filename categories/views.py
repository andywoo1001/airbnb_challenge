from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer

# from django.shortcuts import render
from .models import Category

# Create your views here.


@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":

        all_categoreis = Category.objects.all()
        serializer = CategorySerializer(all_categoreis, many=True)
        return Response(
            serializer.data,
        )
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"created": True})
        else:
            return Response(serializer.errors)


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(
        serializer.data,
    )
