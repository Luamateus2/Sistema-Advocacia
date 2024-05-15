from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth import get_user_model

def login(request):
    return render(request,'tasks/index.html')

def processo(request):
    return render(request,'tasks/processos.html')

def cadastro_usuario(request):
    return render(request,'tasks/cadastro.html')

def tarefas(request):
    return render(request,'tasks/tarefas.html')

def cliente(request):
    return render(request, 'tasks/cliente.html')

def cadastrar_cliente(request):
    pass

def logar(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Certifique-se de usar a função login correta do Django
            login(request, user)
            print('autenticado')
            # Certifique-se de que 'home' é o nome correto da URL para a página inicial
            return redirect(reverse('home'))
        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'tasks/index.html')

    return render(request, 'tasks/index.html')

def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')

        if password != confirmar_senha:
            return render(request, 'tasks/cadastro.html')

        Usuario = get_user_model()
        try:
            novo_usuario = Usuario.objects.create_user(
            email=email, nome=nome, password=password)
            return redirect('login')
        except Exception as e:
            return render(request, 'tasks/cadastro.html')
    else:
       return render(request, 'tasks/cadastro.html')

