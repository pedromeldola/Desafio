from django.contrib import admin
from .models import Jogo
# Register your models here.

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display=['idJogo', 'placar']