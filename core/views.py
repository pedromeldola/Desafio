from django.shortcuts import render,redirect
from .models import Jogo
from django.views.decorators.csrf import csrf_protect

def home_page(request):
    return render(request, 'home.html')

def consultar(request):
    jogo = Jogo.objects.filter()
    return render (request,'consulta.html',{'jogo':jogo})

def inserir(request):
    idJogo = request.POST.get('nJogo')
    placar = request.POST.get('nPlacar')
    
    placarMin1 = Jogo.objects.last(placarMin)
    print(placarMin1)
    placarMin = int(placarMin1)
    placar = int(placar)

    if placar < placarMin:
        placarMin = placar
    else:
        placarMin = placarMin 


    jogo = Jogo.objects.create(idJogo=idJogo,placar=placar,placarMin=placarMin,placarMax=placarMax,quebraRecMin=quebraRecMin,quebraRecMax=quebraRecMax)

    return redirect('/')   