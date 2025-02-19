from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome
