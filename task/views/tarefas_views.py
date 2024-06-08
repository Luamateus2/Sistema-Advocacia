from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario,Cliente,Processo
from django.contrib.auth import get_user_model



def tarefa(request):
    if request.method == 'POST':
            titulo_tarefa = request.POST.get('titulo_tarefa')
            data_base = request.POST.get('data_base')
            data_inicial = request.POST.get('data_inicial')
            data_fatal = request.POST.get('data_fatal')
            situacao = request.POST.get('situacao')
            responsavel= request.POST.get('responsavel')
            processo = request.POST.get('processo')
            cliente_cpf = request.POST.get('cliente')

            cliente = Cliente.objects.get(cpf=cliente_cpf)
            try:
                processo = Processo(
                    titulo_tarefa=titulo_tarefa,
                    data_base=data_base,
                    data_inicial=data_inicial,
                    data_fatal=data_fatal,
                    situacao=situacao,
                    responsavel =responsavel,
                    processo = processo,
                    cliente=cliente
                )
            except Exception as e:
                print("Algo deu errado:", e)
                return render(request, 'tasks/tarefas.html')  
            tarefas.save()
    else:
        print("NEM TENTOU")
        return render(request, 'tasks/tarefas.html')

    return render(request, 'tasks/tarefas.html')

def andamento(request):
  pass