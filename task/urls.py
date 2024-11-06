from django.urls import path
from .views import login_views, processo_views, tarefa_views, cliente_views,cadastar_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',view = login_views.autenticar_usuario,name='autenticar_usuario'),
    
    path('adicionar/usuario',cadastar_views.adicionar_usuario, name='adicionar_usuario'),
    
    path('adicionar/cliente',view=cliente_views.adicionar_cliente,name='adicionar_cliente'),
    path('editar_cliente/<int:cliente_id>/',view=cliente_views.editar_cliente, name='editar_cliente'),
    path('excluir/cliente/<int:cliente_id>/',view=cliente_views.excluir_cliente, name='excluir_cliente'),

    path('adicionar/processo', view=processo_views.adicionar_processo,name='adicionar_processo'),

    path('tarefa',view=tarefa_views.tarefa,name='tarefa'),
    path('editar_tarefa/<int:tarefa_id>/',  view=tarefa_views.editar_tarefa, name='editar_tarefa'),
    path('excluir/tarefa/<int:tarefa_id>/',view=tarefa_views.excluir_tarefa, name='excluir_tarefa'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


