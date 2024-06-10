from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Cliente, Processo


def adicionar_processo(request):
    if request.method == 'POST':
        numero_processo = request.POST.get('numero_processo')
        autor = request.POST.get('autor')
        reu = request.POST.get('reu')
        instancia = request.POST.get('instancia')
        forum = request.POST.get('forum')
        valor_da_causa = request.POST.get('valor_da_causa')
        assunto = request.POST.get('assunto')
        cliente_cpf = request.POST.get('cliente')

        try:
            cliente = Cliente.objects.get(cpf=cliente_cpf)
            processo = Processo(
                numero_processo=numero_processo,
                autor=autor,
                reu=reu,
                instancia=instancia,
                forum=forum,
                valor_da_causa=valor_da_causa,
                assunto=assunto,
                cliente=cliente
            )
            processo.save()
            messages.success(request, 'Processo adicionado com sucesso!')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
        return render(request,'task/processo.html')
    return render(request, 'tasks/processo.html')


def editar_processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    if request.method == 'POST':
        processo.numero_processo = request.POST.get('numero_processo')
        processo.autor = request.POST.get('autor')
        processo.reu = request.POST.get('reu')
        processo.instancia = request.POST.get('instancia')
        processo.forum = request.POST.get('forum')
        processo.valor_da_causa = request.POST.get('valor_da_causa')
        processo.assunto = request.POST.get('assunto')
        cliente_cpf = request.POST.get('cliente')

        try:
            processo.cliente = Cliente.objects.get(cpf=cliente_cpf)
            processo.save()
            messages.success(request, 'Processo atualizado com sucesso!')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
        except Exception as e:
            messages.error(request, f'Algo deu errado: {e}')
        return redirect('processos')

    context = {'processo': processo}
    return render(request, 'tasks/editar_processo.html', context)


def excluir_processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    if request.method == 'POST':
        processo.delete()
        messages.success(request, 'Processo excluído com sucesso!')
        return HttpResponseRedirect(reverse('processos'))

    context = {'processo': processo}
    return redirect(request, 'tasks/excluir_processo.html', context)
