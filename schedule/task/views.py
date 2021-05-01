from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import tasks

# Create your views here.
def index(request):
    task = tasks.objects.all()
    return render(request, 'index.html', {'task': task})

def addtask(request):
    item = request.GET["task"]
    tasks.objects.create(task=item)
    return HttpResponseRedirect('/')

def delete(request,pk):
    try:
        task = tasks.objects.get(pk = pk)
        tasks.objects.get(pk = pk).delete()
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

    
    
