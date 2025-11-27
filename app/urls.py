from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.salvarUsuario, name="salvarUsuario"),
    path("login/", views.loginUsuario, name="loginUsuario"),
    path("logout/", views.logoutUsuario, name="logoutUsuario"),

    #contato
    path("contato/", views.salvarContato, name="salvarContato"),

    #comprar
    path("comprar/<int:id_prod>", views.comprar, name="comprar"),
    path("finalizar-compra/<int:id_prod>", views.finalizarCompra, name="finalizarCompra"),
    path("perfil", views.perfil, name="perfil"),
]
