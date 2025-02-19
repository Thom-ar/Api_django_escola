from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Aluno, Turma
from .serializers import AlunoSerializer, TurmaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
