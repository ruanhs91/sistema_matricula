from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.criar_aluno, name='criar_aluno'),
    path('<int:id>/detalhes/', views.detalhar_aluno, name='detalhar_aluno'),
    path('editar/<int:id>/', views.aluno_editar, name='editar_aluno'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]

