from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario,Cliente,Processo
from django.contrib.auth import get_user_model



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
    return render(request, 'tasks/processos.html')


