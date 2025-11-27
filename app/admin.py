from django.contrib import admin
from app.models import Pagina, Produto, Contato, Pedido
# Register your models here.

#pagina
@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("nome_do_site", "email", "whatsapp", "criado_em")
    ordering = ("nome_do_site",)
    #search_fields = ("nome_do_site", "email")

#produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "criado_em")
    ordering = ("nome",)
    search_fields = ("nome",)
    list_filter = ("criado_em",)

#contato
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "criado_em")
    search_fields = ("nome", "email")
    ordering = ("-criado_em",)

#pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "produto", "quantidade", "total", "data")
    search_fields = ("usuario__username", "produto__nome")
    list_filter = ("data",)
    ordering = ("-data",)
