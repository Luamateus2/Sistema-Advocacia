from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Cliente


def adicionar_cliente(request):
    if request.method == 'POST':
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

        try:
            numero_casa = int(numero_casa)
        except (ValueError, TypeError):
            messages.error(request, "Número da casa inválido.")
            return render(request, 'tasks/processos.html')

        if not nome or not rg or not cpf or not contato or not genero or not data_nascimento or not cep or not logradouro or not bairro:
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
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
            messages.success(request, "Cliente adicionado com sucesso!")
            return redirect('adicionar_cliente')
        except Exception as e:
            messages.error(
                request, f"Ocorreu um erro ao adicionar o cliente: {e}")
            return render(request, 'tasks/cliente.html')

    clientes = Cliente.objects.all()
    return render(request, 'tasks/cliente.html', {'clientes': clientes})
