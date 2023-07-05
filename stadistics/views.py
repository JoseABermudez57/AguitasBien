from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Watersample
import json, datetime

# Create your views here.
@csrf_exempt
def save_water_sample(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Método no permitido.'})
    else:
        data = json.loads(request.body)
        ph = float(data.get('ph', 0.0))
        condu = float(data.get('condu', 0.0))
        termo = float(data.get('termo', 0.0))
        otro_sensor = float(data.get('otroSensor', 0.0))

        sensor_data = Watersample(timestamp = datetime.datetime.now(),ph=ph, condu=condu, termo=termo, otroSensor=otro_sensor)
        sensor_data.save()
    
        return JsonResponse({'message': 'Datos guardados correctamente.', 'status': True})

