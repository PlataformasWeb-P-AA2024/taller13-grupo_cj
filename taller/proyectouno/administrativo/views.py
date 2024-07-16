from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.models import *
from administrativo.serializers import UserSerializer, GroupSerializer, \
EdificioSerializer, DepartamentoSerializer

# crear vistas a través de viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        """
        valor = self.request.query_params
        print(valor)
        if 'nombre' in valor.keys():
            return Edificio.objects.filter(nombre=valor['nombre']).all()
        else:
            if 'correo' in valor.keys():
                return Edificio.objects.filter(correo__contains=valor['correo']).all()
            else:
                return Edificio.objects.all()


# class NumeroTelefonicoViewSet(viewsets.ModelViewSet):
class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = Departamento
    # permission_classes = [permissions.IsAuthenticated]
