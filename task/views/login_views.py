from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario,Cliente,Processo
from django.contrib.auth import get_user_model

# APAGAR DEF LOGIN

def autenticar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('autenticado')
            return redirect(reverse('processos')) # MUDEI COLOCAR HOME
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
    return render(request,'tasks/cadastro.html')
