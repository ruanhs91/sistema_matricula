from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class Aluno(admin.ModelAdmin):
    list_display=('nome', 'numero_matricula', 'curso', 'serie', 'turno')
    list_filter = ('curso', 'serie', 'turno', 'uf')
    search_field=('nome', 'numero_matricula', 'cpf', 'email')
# Register your models here.
