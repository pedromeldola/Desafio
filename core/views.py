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
    
    placarMin1 = Jogo.objects.latest('placarMin').placarMin
    placarMax1 = Jogo.objects.latest('placarMax').placarMax
    quebraRecMin1 = Jogo.objects.latest('quebraRecMin').quebraRecMin
    quebraRecMax1 = Jogo.objects.latest('quebraRecMax').quebraRecMax
    
    placar1 = int(placar)
    placarMin = int(placarMin1)
    placarMax = int(placarMax1)
    quebraRecMin = int(quebraRecMin1)
    quebraRecMax = int(quebraRecMax1)




    if placar1 > placarMax:
        placarMax = placar1
        quebraRecMax = quebraRecMax+1
        placarMin = placarMin
    elif placar1 < placarMin:
        placarMin = placar1
        quebraRecMin = quebraRecMin+ 1
    else:
        quebraRecMin = quebraRecMin+ 0 
        quebraRecMmax =quebraRecMax+ 0     


   
    jogo = Jogo.objects.create(idJogo=idJogo,placar=placar,placarMin=placarMin,placarMax=placarMax,quebraRecMin=quebraRecMin,quebraRecMax=quebraRecMax)
    jogo.save()
    
    return redirect('/')   