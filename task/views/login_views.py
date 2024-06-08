from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from ..models import Usuario
from django.contrib.auth import get_user_model

# APAGAR DEF LOGIN

def autenticar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('autenticado')
            return redirect(reverse('adicionar_cliente'))
        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'tasks/index.html')

    return render(request, 'tasks/index.html')

