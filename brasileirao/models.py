from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Jogo(Base):
    liga = models.CharField(max_length=50)
    dataDoJogo = models.DateField()
    hora = models.TimeField()
    nomeTime1 = models.CharField(max_length=30)
    nomeTime2 = models.CharField(max_length=30)
    golsTime1 = models.IntegerField()
    golsTime2 = models.IntegerField()
    escudoTime1 = models.URLField()
    escudoTime2 = models.URLField()

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['id']

    def __str__(self):
        return f'{self.liga} {self.nomeTime1} x {self.nomeTime2} {self.dataDoJogo} às {self.hora}'

