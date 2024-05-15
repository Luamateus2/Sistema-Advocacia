from django.urls import path
from . import views

urlpatterns = [
    path('',view = views.login,name='login'),
    path('logar',view=views.logar,name='logar'),
    
    path('cadastro/usuario', view=views.cadastro_usuario, name='cadastro_usuario'),   
    path('adicionar/usuario',views.adicionar_usuario, name='adicionar_usuario'),
    
    path('processos',view=views.processo,name='processos'),
    path('tarefas',view=views.tarefas,name='tarefas'),
    path('cadastro/cliente', view=views.cliente, name='cadastro/cliente'),
    path('cadastar/cliente',view=views.cadastrar_cliente,name='cadastrar_cliente'),

]
