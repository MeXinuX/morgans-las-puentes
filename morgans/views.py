from django.shortcuts import render

def index(request):
    return render(request, 'index.html' )

def menu(request):
    return render(request, 'menu.html')

def sucursales(request):
    return render(request, 'sucursales.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def unete(request):
    return render(request, 'unete.html')
