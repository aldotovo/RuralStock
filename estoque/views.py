from django.shortcuts import render
from .models import Movimentacao
from collections import defaultdict

import json

def dashboard(request):
    movimentacoes = Movimentacao.objects.all()

    entrada = defaultdict(float)
    saida = defaultdict(float)

    for m in movimentacoes:
        if m.tipo == 'E':
            entrada[m.produto.nome] += m.quantidade
        else:
            saida[m.produto.nome] += m.quantidade

    produtos = list(set(list(entrada.keys()) + list(saida.keys())))

    dados_entrada = [entrada[p] for p in produtos]
    dados_saida = [saida[p] for p in produtos]

    context = {
        'produtos': json.dumps(produtos),
        'entrada': json.dumps(dados_entrada),
        'saida': json.dumps(dados_saida),
    }


    return render(request, 'dashboard.html', context)