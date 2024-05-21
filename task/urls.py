from django.urls import path
from . import views

urlpatterns = [
    # MUDOU AQUI
    path('',view = views.autenticar_usuario,name='autenticar_usuario'),
    # path('autenticar/login',view=views.autenticar_usuario,name='autenticar_usuario'),
    
    path('cadastrar/usuario', view=views.cadastrar_usuario, name='cadastrar_usuario'),   
    path('adicionar/usuario',views.adicionar_usuario, name='adicionar_usuario'),
    
    path('cadastrar/cliente', view=views.cliente, name='cadastro/cliente'),
    path('adicionar/cliente',view=views.adicionar_cliente,name='adicionar_cliente'),
   
    path('adicionar/processo',view=views.adicionar_processo,name='adicionar_processo'),
    path('processos',view=views.processo,name='processos'),
    
    path('tarefas',view=views.tarefas,name='tarefas'),
    

]
