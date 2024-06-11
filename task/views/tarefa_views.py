from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Tarefa


def tarefa(request):

    if request.method == 'POST':
        titulo_tarefa = request.POST.get('titulo_tarefa')
        data_base = request.POST.get('data_base')
        data_inicial = request.POST.get('data_inicial')
        data_fatal = request.POST.get('data_fatal')
        situacao = request.POST.get('situacao')
        responsavel = request.POST.get('responsavel')
        processo = request.POST.get('processo')
        if not titulo_tarefa or not data_base or not data_fatal or not data_inicial or not situacao or not responsavel or not processo :
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/processo.html')
        try:
            tarefa = Tarefa(
                titulo_tarefa=titulo_tarefa,
                data_base=data_base,
                data_inicial=data_inicial,
                data_fatal=data_fatal,
                situacao=situacao,
                responsavel=responsavel,
                processo=processo,
              
            )
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
     
        except Exception as e:
            messages.error(request, f'Algo deu errado: {e}')
        return redirect('tarefa')


    return render(request, 'tasks/tarefa.html')

    clientes = Cliente.objects.all()
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.titulo_tarefa = request.POST.get('titulo_tarefa')
        tarefa.data_base = request.POST.get('data_base')
        tarefa.data_inicial = request.POST.get('data_inicial')
        tarefa.data_fatal = request.POST.get('data_fatal')
        tarefa.situacao = request.POST.get('situacao')
        tarefa.responsavel = request.POST.get('responsavel')
        tarefa.processo = request.POST.get('processo')
        cliente_cpf = request.POST.get('cliente')
        try:
            tarefa.cliente = Cliente.objects.get(cpf=cliente_cpf)
            tarefa.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
        except Exception as e:
            messages.error(request, f'Algo deu errado: {e}')
        return redirect('tarefa')

    context = {'tarefa': tarefa}
    return render(request, 'tasks/editar_tarefa.html', context)


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tarefa')

    context = {'tarefa': tarefa}
    return redirect(request, 'tasks/tarefa.html', context)
