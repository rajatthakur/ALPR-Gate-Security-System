from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from PIL import Image
from pytesseract import *
from datetime import datetime
import cv2
# Importing the Opencv Library
import numpy as np
from rest_framework.views import APIView
from.serializers import CarPlateSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CarPlate
# Create your views here.

def index(request):
    return render(request,'queryform.html')

def formsubmit(request):
    cars = CarPlate.objects.filter(numplate = request.POST['car_plate'])
    from extractMod import extractImg

    number = extractImg()

    car = CarPlate()
    car.numplate = number
    car.inTime = datetime.now()
    car.outTime = datetime.now()
    car.save()

    return render(request,'cardetails.html',{'cars' : cars})

class CarEntry(APIView):
    def post(self,request):
        car = CarPlate()
        car.numplate = request.POST['car_plate']
        car.inTime = datetime.now()
        # car.outTime = datetime.now()
        car.save()
        return Response(status=status.HTTP_200_OK)

class CarExit(APIView):
    def post(self,request):
        cars = CarPlate.objects.filter(numplate=request.POST['car_plate'],outTime = None)
        for car in cars:
            car.outTime = datetime.now()
            car.save()
        return Response(status=status.HTTP_200_OK)



class CarQuery(APIView):
    def post(self,request):
        cars = CarPlate.objects.filter(numplate=request.POST['car_plate'])
        serial = CarPlateSerializer(cars, many=True)
        return Response(serial.data)
