from django.shortcuts import render, redirect
from .models import DadosFormulario

def index(request):
    return render(
        request,
        'pages/index.html'    
    )

def planos(request):
    return render(
        request,
        'pages/planos.html'    
    )
    
def pedido1(request):
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # Obtenha os outros campos conforme necessário

        # Salve os dados no banco de dados
        DadosFormulario.objects.create(usuario=usuario, email=email, senha=senha)

        return redirect('https://mpago.la/17HgaHB')
    
    return render(
        request,
        'pages/pedidos/pedido_conhecido.html'
    )

def pedido2(request):
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # Obtenha os outros campos conforme necessário

        # Salve os dados no banco de dados
        DadosFormulario.objects.create(usuario=usuario, email=email, senha=senha)

        return redirect('https://mpago.la/2zG82w4')
    
    return render(
        request,
        'pages/pedidos/pedido_popular.html'
    )

def pedido3(request):
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # Obtenha os outros campos conforme necessário

        # Salve os dados no banco de dados
        DadosFormulario.objects.create(usuario=usuario, email=email, senha=senha)

        return redirect('https://mpago.la/2zmbbgT')
    
    return render(
        request,
        'pages/pedidos/pedido_famoso.html'
    )

def contato(request):
    return render(
        request,
        'pages/contato.html'
    )
    
def sobre(request):
    return render(
        request,
        'pages/sobre.html'
    )
