from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import json
# Create your views here.
def data_load():
    js = []
    data = Task.objects.all()
    for row in data:
        js.append({'id': row.id, 'task': row.name, 'done': row.done})
    return js

@csrf_exempt
def todo_response(request, id=None):
    if request.method == 'GET':

        return JsonResponse(data_load(), safe=False)
    elif request.method == 'POST':
        js_data = json.loads(request.body.decode())
        task = Task(name=js_data['task'])
        task.save()

        return JsonResponse(data_load(), safe=False)
    elif request.method == 'PUT':

        task = Task.objects.get(id=id)
        task.done = not task.done
        task.save()

        return JsonResponse({'id': task.id, 'task': task.name, 'done': task.done})
    elif request.method ==  'DELETE':

        task = Task.objects.get(id=id)
        task.delete()

        return HttpResponse("")
    return HttpResponse(status=200)
