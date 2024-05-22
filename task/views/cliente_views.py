from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario,Cliente,Processo
from django.contrib.auth import get_user_model


def adicionar_cliente(request):
    if request.method == 'POST':
        print("Método POST recebido.")
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        data_nascimento = request.POST.get('data_nascimento')
        contato = request.POST.get('contato')
        email = request.POST.get('email')
        genero = request.POST.get('genero')
        whatsapp = request.POST.get('whatsapp')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_casa = request.POST.get('numero_casa')
        bairro = request.POST.get('bairro')

        # Verificação e conversão do campo numero_casa
        try:
            numero_casa = int(numero_casa)
        except (ValueError, TypeError):
            print("Número da casa inválido.")
            return render(request, 'tasks/processos.html')

        try:
            novo_cliente = Cliente(
                nome=nome,
                cpf=cpf,
                rg=rg,
                data_nascimento=data_nascimento,
                contato=contato,
                email=email,
                genero=genero,
                whatsapp=whatsapp,
                cep=cep,
                logradouro=logradouro,
                numero_casa=numero_casa,
                bairro=bairro
            )
            novo_cliente.save()
            print("Deu certo")
            # Substitua 'success_page' pelo nome correto da URL de sucesso
            return redirect('logar')

        except Exception as e:
            print("Algo deu errado:", e)
            return render(request, 'tasks/cliente.html')

    else:
        print("Nem tentou")
        return render(request, 'tasks/cliente.html')