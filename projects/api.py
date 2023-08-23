from .models import Projects
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Projects.objects.all() # Consulta todos los datos de una tabla
  permission_classes = [permissions.AllowAny] # Indico que cualquiera pueda acceder a la API
  serializer_class = ProjectSerializer