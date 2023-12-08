from django.urls import path
from instagram.views import index, contato, planos, pedido1, pedido2, pedido3, sobre

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('sobre-nós/', sobre, name='sobre'),
    path('planos/', planos, name='planos'),
    path('pedido/instagram-conhecido', pedido1, name='pedido1'),
    path('pedido/instagram-popular', pedido2, name='pedido2'),
    path('pedido/instagram-famoso', pedido3, name='pedido3'),
]
