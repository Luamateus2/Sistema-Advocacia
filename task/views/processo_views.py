from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Cliente, Processo


from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Cliente, Processo


def adicionar_processo(request):
    if request.method == 'POST':
        numero_processo = request.POST.get('numero_processo')
        autor_cpf = request.POST.get('autor')
        reu = request.POST.get('reu')
        instancia = request.POST.get('instancia')
        forum = request.POST.get('forum')
        valor_da_causa = request.POST.get('valor_da_causa')
        assunto = request.POST.get('assunto')

        try:
            autor = Cliente.objects.get(cpf=autor_cpf)
            processo = Processo(
                numero_processo=numero_processo,
                autor=autor,
                reu=reu,
                instancia=instancia,
                forum=forum,
                valor_da_causa=valor_da_causa,
                assunto=assunto
            )
            processo.save()
            messages.success(request, 'Processo adicionado com sucesso!')
            return render(request,'tasks/processo.html')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
            return render(request, 'tasks/processo.html', {'clientes': Cliente.objects.all()})

    clientes = Cliente.objects.all()
    return render(request, 'tasks/processo.html', {'clientes': clientes})



def excluir_processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    if request.method == 'POST':
        processo.delete()
        messages.success(request, 'Processo excluído com sucesso!')
        return HttpResponseRedirect(reverse('processos'))

    context = {'processo': processo}
    return redirect(request, 'tasks/excluir_processo.html', context)
