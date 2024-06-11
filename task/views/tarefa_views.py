from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.dateparse import parse_date
from ..models import Tarefa, Processo


def tarefa(request):
    if request.method == 'POST':
        titulo_tarefa = request.POST.get('titulo_tarefa')
        data_inicial = request.POST.get('data_inicial')
        data_fatal = request.POST.get('data_fatal')
        situacao = request.POST.get('situacao')
        responsavel = request.POST.get('responsavel')
        numero_processo = request.POST.get('processo')

        if not titulo_tarefa or not data_fatal or not data_inicial or not situacao or not responsavel or not numero_processo:
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/tarefa.html')

        data_inicial_parsed = parse_date(data_inicial)
        data_fatal_parsed = parse_date(data_fatal)

        if data_fatal_parsed < data_inicial_parsed:
            messages.error(
                request, "A data fatal não pode ser inferior à data inicial.")
            return render(request, 'tasks/tarefa.html')

        try:
            processo = Processo.objects.get(numero_processo=numero_processo)
        except Processo.DoesNotExist:
            messages.error(request, "O processo especificado não existe.")
            return render(request, 'tasks/tarefa.html')

        try:
            tarefa = Tarefa(
                titulo_tarefa=titulo_tarefa,
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

    tarefas = Tarefa.objects.all()
    processos = Processo.objects.all()
    return render(request, 'tasks/tarefa.html', {'tarefas': tarefas, 'processos': processos})


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        titulo_tarefa = request.POST.get('titulo_tarefa')
        data_inicial = request.POST.get('data_inicial')
        data_fatal = request.POST.get('data_fatal')
        situacao = request.POST.get('situacao')
        responsavel = request.POST.get('responsavel')

        if not titulo_tarefa or not data_fatal or not data_inicial or not situacao or not responsavel:
            messages.error(
                request, "Todos os campos obrigatórios devem ser preenchidos.")
            return render(request, 'tasks/editar_tarefa.html', {'tarefa': tarefa})

        data_inicial_parsed = parse_date(data_inicial)
        data_fatal_parsed = parse_date(data_fatal)

        if data_fatal_parsed < data_inicial_parsed:
            messages.error(
                request, "A data fatal não pode ser inferior à data inicial.")
            return render(request, 'tasks/editar_tarefa.html', {'tarefa': tarefa})

        tarefa.titulo_tarefa = titulo_tarefa
        tarefa.data_inicial = data_inicial
        tarefa.data_fatal = data_fatal
        tarefa.situacao = situacao
        tarefa.responsavel = responsavel

        try:
            tarefa.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('tarefa')
        except Exception as e:
            messages.error(request, f'Algo deu errado: {e}')
            return render(request, 'tasks/editar_tarefa.html', {'tarefa': tarefa})

    context = {'tarefa': tarefa}
    return render(request, 'tasks/editar_tarefa.html', context)

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tarefa')

    context = {'tarefa': tarefa}
    return redirect(request, 'tasks/editar_tarefa.html', context)
