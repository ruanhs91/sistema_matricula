from django.db import models

class Aluno(models.Model):
    sexo_opcoes=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    curso_opcoes=[
        ('a', 'Apicultura'),
        ('b', 'Alimentos'),
        ('i', 'Informática'),
    ]
    
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    sexo = models.CharField(max_length=1, choices=sexo_opcoes)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade=models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField()
    endereco = models.CharField()
    numero = models.CharField()
    complemento = models.CharField()
    bairro = models.CharField()
    uf = models.CharField(max_length=2)
    numero_matricula = models.CharField(unique=True)
    curso = models.CharField(max_length=1,choices=curso_opcoes)
    serie=models.CharField()
    turno = models.CharField()
    observacoes=models.TextField(max_length=200)
    
    def __str__(self):
        return self.nome
    
    
