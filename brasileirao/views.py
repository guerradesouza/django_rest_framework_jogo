from rest_framework import generics

from rest_framework import viewsets

from .models import Jogo
from .serializers import JogoSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = (permissions.DjangoModelPermissions, IsAuthenticated )


'''
class JogosAPIView(generics.ListCreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class JogoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
'''