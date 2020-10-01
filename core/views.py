from django.shortcuts import render,redirect
from .models import Jogo
from django.views.decorators.csrf import csrf_protect

def home_page(request):
    jogo = Jogo.objects.all()
    return render (request,'home.html',{'jogo':jogo})

def inserir(request):
    placar = request.POST.get('nPlacar')
    
    try:
        placarMin = int(Jogo.objects.earliest('placarMin').placarMin)
        placarMax = int(Jogo.objects.latest('placarMax').placarMax)
        quebraRecMin = int(Jogo.objects.latest('quebraRecMin').quebraRecMin)
        quebraRecMax = int(Jogo.objects.latest('quebraRecMax').quebraRecMax)
    except:
        placarMin = False
        placarMax = False
        quebraRecMin = False
        quebraRecMax = False
        
    placar = int(placar)

    if placarMin is False:
        placarMin = placar
        placarMax = placar
    elif placar < placarMin:
        placarMin = placar
        quebraRecMin += 1
    elif placar > placarMax or placarMax is False:
        placarMax = placar
        quebraRecMax += 1
    else:
        quebraRecMin = quebraRecMin+ 0 
        quebraRecMmax = quebraRecMax+ 0     
        
    jogo = Jogo.objects.create(placarMin=placarMin,placar=placar,placarMax=placarMax,quebraRecMin=quebraRecMin,quebraRecMax=quebraRecMax)
    return redirect('/')  