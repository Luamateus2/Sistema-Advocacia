from django.urls import path
from . import views

urlpatterns = [
    path('',view = views.login,name='login'),
    path('cadastro_usuario', view=views.cadastro_usuario, name='cadastro_usuario'),
    path('processos',view=views.processo,name='processos'),
    path('tarefas',view=views.tarefas,name='tarefas'),
    path('cadastro_cliente', view=views.cliente, name='Cadastro cliente'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),

]
