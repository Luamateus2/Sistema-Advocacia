from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Cliente

# Função para excluir cliente


def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return render(request,'tasks/cliente.html')

    return render(request, 'tasks/cliente.html')
