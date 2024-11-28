from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Skill(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    nivel = models.IntegerField(default=1)

    def clean(self):
        if Skill.objects.filter(nome=self.nome).exists():
            raise ValidationError({'nome': 'Já existe uma skill com este nome no sistema.'})
        
        #if self.pk and self.cargo_set.exists():
            #raise ValidationError({'nome': 'Esta skill está associada a um cargo.'})

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, blank=True)

    def clean(self):
        if Cargo.objects.filter(nome=self.nome).exists():
            raise ValidationError({'nome': 'Já existe um cargo com este nome no sistema.'})
        

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    gestor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="funcionarios")

    def __str__(self):
        return self.nome

class CalendarioItem(models.Model):
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.titulo} em {self.data_inicio}"
