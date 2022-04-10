from rest_framework import serializers

from .models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = (
            'id',
            'liga',
            'dataDoJogo',
            'hora',
            'nomeTime1',
            'nomeTime2',
            'golsTime1',
            'golsTime2',
            'escudoTime1',
            'escudoTime2',
        )