from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Usuario



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

def cadastrar_usuario(request):
     if request.method == 'POST':
        # Se o formulário foi submetido, obtenha os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verifica se as senhas são iguais
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'tasks/cadastro.html')

        # Cria uma instância do modelo Usuario com os dados do formulário
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)

        # Salva o novo usuário no banco de dados
        novo_usuario.save()

        # Adiciona uma mensagem de sucesso
        messages.success(request, 'Usuário cadastrado com sucesso!')

        # Redireciona para a página de login
        # Substitua 'nome_da_view_do_login' pela sua view de login
        return redirect('login')
     else:
        # Se o método da requisição não for POST, renderize o template do formulário
        return render(request, 'seu_template_de_cadastro.html')