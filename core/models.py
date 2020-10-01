from django.db import models

#criação da classe com os atributos
class Jogo(models.Model):
    idJogo = models.AutoField(primary_key=True)
    placar = models.IntegerField()
    placarMin = models.IntegerField()
    placarMax = models.IntegerField()
    quebraRecMin = models.IntegerField()
    quebraRecMax = models.IntegerField()

    def __str__(self):
        return str(self.idJogo)

