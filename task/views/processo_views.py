from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def adicionar_processo(request):
    if request.method == 'POST':
        numero_processo = request.POST.get('numero_processo')
        autor_cpf = request.POST.get('autor')
        reu = request.POST.get('reu')
        instancia = request.POST.get('instancia')
        forum = request.POST.get('forum')
        valor_da_causa = request.POST.get('valor_da_causa')
        assunto = request.POST.get('assunto')
        if Processo.objects.filter(numero_processo=numero_processo).exists():
            messages.error(request, 'O número do processo já existe.')
        if not numero_processo or not autor_cpf or not reu or instancia or forum or valor_da_causa or assunto :
              messages.error(request, "Todos os campos obrigatórios devem ser preenchidos.")
              return render(request, 'tasks/processo.html')
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



