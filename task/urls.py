from django.urls import path
from .views import processo_views, tarefa_views, cliente_views,cadastar_views,user_views,client_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',view = user_views.authenticate_user,name='login'),


    
    path('adicionar/usuario',user_views.add_user, name='adicionar_usuario'),
    




    path('adicionar/cliente',view=client_views.add_client,name='adicionar_cliente'),



    path('editar_cliente/<int:cliente_id>/',view=cliente_views.editar_cliente, name='editar_cliente'),
    path('excluir/cliente/<int:cliente_id>/',view=cliente_views.excluir_cliente, name='excluir_cliente'),

    path('adicionar/processo', view=processo_views.adicionar_processo,name='adicionar_processo'),

    path('tarefa',view=tarefa_views.tarefa,name='tarefa'),
    path('editar_tarefa/<int:tarefa_id>/',  view=tarefa_views.editar_tarefa, name='editar_tarefa'),
    path('excluir/tarefa/<int:tarefa_id>/',view=tarefa_views.excluir_tarefa, name='excluir_tarefa'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


