from django.shortcuts import render

def lista_aldeias(request):
    return render(request, 'aldeias/lista.html')
