from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Cliente


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

        cliente.save()
        messages.success(request, 'Cliente atualizado com sucesso!')
        return redirect('cliente')

    context = {
        'cliente': cliente
    }
    return render(request, 'tasks/editar_cliente.html', context)
