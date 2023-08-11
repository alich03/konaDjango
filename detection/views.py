from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .object_detection import detect_objects
import requests
from rest_framework.views import APIView
from PIL import Image
import numpy as np
import base64
import io


@api_view(['POST', 'GET'])
def process_image(request):
    base64_image = request.data.get('image')  # Change this line

    if base64_image:
        image_data = base64.b64decode(base64_image)
        image_array = Image.open(io.BytesIO(image_data))

        # image_data = base64.b64decode(base64_image)
        # image_array = np.load(io.BytesIO(image_data))
        # print(image_array)
        msg = " Done "
        alldata=detect_objects(image_array)
        
        return Response({'msg': msg,'dta':alldata})
    else:
        return Response({'e': 'No image data found in the request'})



@api_view(['POST','GET'])
def upload_image(request):
    if 'image' in request.FILES:
        uploaded_image = request.FILES['image']
        # detection_results = detect_objects(uploaded_image)
        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
    return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST','GET'])
def test1(request):
    
    return Response({'msg': 'ok'})

