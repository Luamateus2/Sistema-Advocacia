from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages  # Importe o módulo de mensagens

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Defina as URLs que podem ser acessadas sem autenticação
        open_urls = [
            reverse('autenticar_usuario'),  # URL para a página de login
            reverse('adicionar_usuario')    # URL para a página de cadastro
        ]
        
        # Se o usuário não estiver autenticado e não estiver acessando as páginas abertas, redirecione para a página de login
        if not request.user.is_authenticated and request.path not in open_urls:
            messages.error(request, "Você precisa estar logado para acessar essa página.")  # Adiciona a mensagem de erro
            return redirect('autenticar_usuario')  # Redireciona para o login
        
        # Caso contrário, prossiga com o processamento normal da resposta
        response = self.get_response(request)
        return response
