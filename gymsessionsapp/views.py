from django.shortcuts import get_object_or_404
from .serializers import AthleteSerializer
from .models import Athlete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core import serializers

class manageAthletes(APIView):
    @swagger_auto_schema(
        operation_description="get an athlete by ID",
        responses={200: 'Success', 400: 'Bad Request'},
        manual_parameters=[
           #openapi.Parameter('param', openapi.IN_QUERY, description="athlete name", type=openapi.TYPE_STRING),
        ],
    )
    def get(self, request: HttpRequest, id: int):
        output_athlete = Athlete.objects.get(pk=id)
        return JsonResponse(output_athlete.serialize()) #TODO may be better with serializers
    
    @swagger_auto_schema(request_body=AthleteSerializer)
    def post(self, request: HttpRequest,id: int):
        athlete = get_object_or_404(Athlete,pk=id)
        serializer = AthleteSerializer(athlete, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="get an athlete by ID",
        responses={200: 'Success', 400: 'Bad Request'},
        manual_parameters=[
           #openapi.Parameter('param', openapi.IN_QUERY, description="athlete name", type=openapi.TYPE_STRING),
        ],
    )
    def delete(self, request: HttpRequest, id: int):
        athlete = Athlete.objects.get(pk=id)
        if(athlete):
            athlete.delete()
            return JsonResponse({'success': 'True'},status=status.HTTP_200_OK)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    
class createAthletes(APIView):
    
    @swagger_auto_schema(request_body=AthleteSerializer)
    def put(self, request: HttpRequest):
        serializer = AthleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)