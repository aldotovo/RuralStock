from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto, Movimentacao       

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade_atual', 'unidade')
    search_fields = ('nome',)
    list_filter = ('categoria',)

    def estoque_baixo(self, obj):
        return obj.quantidade_atual < 10  # limite simples

    estoque_baixo.boolean = True
    estoque_baixo.short_description = "Estoque baixo"


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'tipo', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('produto__nome',)
    ordering = ('-data',)

    