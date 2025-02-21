from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


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
            return render(request, 'tasks/cliente.html')

        if not nome or not rg or not cpf or not contato or not genero or not data_nascimento or not cep or not logradouro or not bairro:
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/cliente.html')

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


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.cpf = request.POST.get('cpf')
        cliente.rg = request.POST.get('rg')
        cliente.data_nascimento = request.POST.get('data_nascimento')
        cliente.genero = request.POST.get('genero')
        cliente.contato = request.POST.get('contato')
        cliente.whatsapp = request.POST.get('whatsapp')
        cliente.email = request.POST.get('email')
        cliente.cep = request.POST.get('cep')
        cliente.logradouro = request.POST.get('logradouro')
        cliente.numero_casa = request.POST.get('numero_casa')
        cliente.bairro = request.POST.get('bairro')
        cliente.pis_pasep = request.POST.get('pis_pasep')
        cliente.serie = request.POST.get('serie')
        cliente.numero = request.POST.get('numero')
        cliente.uf = request.POST.get('uf')

        try:
            cliente.numero_casa = int(cliente.numero_casa)
        except (ValueError, TypeError):
            messages.error(request, "Número da casa inválido.")
            return render(request, 'tasks/editar_cliente.html', {'cliente': cliente})

        if not cliente.nome or not cliente.rg or not cliente.cpf or not cliente.contato or not cliente.genero or not cliente.data_nascimento or not cliente.cep or not cliente.logradouro or not cliente.bairro:
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/editar_cliente.html', {'cliente': cliente})

        try:
            cliente.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente')
        except Exception as e:
            messages.error(request, f'Algo deu errado: {e}')
            return render(request, 'tasks/editar_cliente.html', {'cliente': cliente})

    return render(request, 'tasks/editar_cliente.html', {'cliente': cliente})


def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
    return render(request, 'tasks/cliente.html')

