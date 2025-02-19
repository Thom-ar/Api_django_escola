from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# Compare this snippet from escolaapi/urls.py:
# from django.urls import path, include