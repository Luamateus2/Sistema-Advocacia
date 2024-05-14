from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

def login(request):
    return render(request,'tasks/index.html')

def processo(request):
    return render(request,'tasks/processos.html')

def cadastro_usuario(request):
    return render(request,'tasks/cadastro.html')

def tarefas(request):
    return render(request,'tasks/tarefas.html')

def cliente(request):
    return render(request,'tasks/cliente.html')

def logar(request):
   pass
    
def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')

        if password != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'tasks/cadastro.html')

        Usuario = get_user_model()
        try:
            novo_usuario = Usuario.objects.create_user(
            email=email, nome=nome, password=password)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar usuário: ')
            return render(request, 'tasks/cadastro.html')
    else:
       return render(request, 'tasks/cadastro.html')
