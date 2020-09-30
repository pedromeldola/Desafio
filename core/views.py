from django.shortcuts import render,redirect
from .models import Jogo
from django.views.decorators.csrf import csrf_protect

def home_page(request):
    return render(request, 'home.html')

def consultar(request):
    jogo = Jogo.objects.all()
    return render (request,'consulta.html',{'jogo':jogo})

def inserir(request):
    idJogo = request.POST.get('nJogo')
    placar = request.POST.get('nPlacar')
    
    

    placarMax = Jogo.objects.latest('placarMax').placarMax
    quebraRecMin = Jogo.objects.latest('quebraRecMin').quebraRecMin
    quebraRecMax = Jogo.objects.latest('quebraRecMax').quebraRecMax
    placarMin = Jogo.objects.latest('placarMin').placarMin
    
    placar = int(placar)
    placarMin = int(placarMin)
    placarMax = int(placarMax)
    quebraRecMin = int(quebraRecMin)
    quebraRecMax = int(quebraRecMax)



    if placar > placarMax:
        placarMax = placar
        quebraRecMax = quebraRecMax + 1
        
    elif placar < placarMin:
        placarMin = placar
        quebraRecMin = quebraRecMin + 1
    else:
        quebraRecMin = quebraRecMin+ 0 
        quebraRecMmax =quebraRecMax+ 0     
        
    jogo = Jogo.objects.create(placarMin=placarMin,idJogo=idJogo,placar=placar,placarMax=placarMax,quebraRecMin=quebraRecMin,quebraRecMax=quebraRecMax)
    return redirect('/')  