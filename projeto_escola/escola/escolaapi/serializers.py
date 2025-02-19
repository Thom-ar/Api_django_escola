from rest_framework import serializers
from .models import Aluno, Turma

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, read_only=True)

    class Meta:
        model = Turma
        fields = '__all__'
