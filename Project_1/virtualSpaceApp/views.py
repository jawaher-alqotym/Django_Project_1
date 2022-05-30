from django.shortcuts import render,redirect,resolve_url
from .models import *
from .forms import TaskForm, VrSpaceForm
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    current_user_id = request.user.id
    tasks = Task.objects.filter(user_id=current_user_id)
    vrSpaces = VrSpace.objects.filter(user_id=current_user_id)
    context = {'tasks': tasks, 'vrSpaces': vrSpaces}
    return render(request, 'home.html', context)

def delete(request, Task_id):
    item = Task.objects.get(pk=Task_id)
    item.delete()
    return redirect(resolve_url('home'))


def CreatTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
    if form.is_valid():
        task = Task.objects.create(user = request.user, name = request.POST['name'])
        return redirect(resolve_url('home'))
    context = {'form':form}
    return render(request, 'task_form.html', context)

def UpdateTask(request,Task_id):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.filter(id= Task_id).update(name = request.POST['name'])
        messages.success(request, f'{ Task.objects.get(id= Task_id)} task have been edited!')
        return redirect(resolve_url('home'))
    context = {'form': form}
    return render(request, 'task_form.html', context)

def DeletVrSpace(request, VrSpace_id):
    item = VrSpace.objects.get(pk=VrSpace_id)
    item.delete()
    return redirect(resolve_url('home'))

def CreatVrSpace(request):
    form = VrSpaceForm()
    if request.method == 'POST':
        form = VrSpaceForm(request.POST, request.FILES)
    if form.is_valid():
        print(request.POST, request.FILES or None)
        task = VrSpace.objects.create(user_id = request.user.id, image_field = request.FILES['image_field'], audio_field =  request.FILES['audio_field'] )
        return redirect(resolve_url('home'))
    context = {'form': form}
    return render(request, 'vSpace_form.html', context)



