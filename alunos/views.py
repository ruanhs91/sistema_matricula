from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
    alunos=Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html',{'alunos':alunos})

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else: 
        form =AlunoForm()
    return render(request, 'alunos/form_aluno.html', {'form': form})

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'alunos/form_aluno.html',{'form':form})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('lista_alunos')

def detalhar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'alunos/detalhe.html', {'aluno':aluno})

