from django.urls import path
from .views import login_views, processo_views, tarefas_views,cliente_views

urlpatterns = [
    # MUDOU AQUI
    path('',view = login_views.autenticar_usuario,name='autenticar_usuario'),
    # path('autenticar/login',view=views.autenticar_usuario,name='autenticar_usuario'),
    
    path('adicionar/usuario',login_views.adicionar_usuario, name='adicionar_usuario'),
    
    path('adicionar/cliente',view=cliente_views.adicionar_cliente,name='adicionar_cliente'),
   
    path('adicionar/processo',view=processo_views.adicionar_processo,name='adicionar_processo'),    
    path('tarefas',view=tarefas_views.tarefas,name='tarefas'),
    

]


