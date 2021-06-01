from django.http import request
from django.shortcuts import render,redirect
from .models import cliente
from .forms import clienteForm
# Create your views here.

def inicio(request):
    clientes = cliente.objects.all()      #Select * from cliente
    contexto = {
        'clientes':clientes
    }
    return render(request,'index.html',contexto)

def crearCliente(request):
    if request.method == 'GET':
        form = clienteForm()
        contexto = {
            'form':form
        }
    else:
        form = clienteForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'index.html',contexto)
