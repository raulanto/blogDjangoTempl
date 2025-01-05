from django.shortcuts import render

def index(request):
    return render(request, 'index.html',context={
        'titulo': 'Inicio',
        'texto': 'Este é o texto da página home',
    })