from django.shortcuts import render
from itertools import groupby
from .models import Evento

MESES_PT = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro',
}


def index(request):
    categoria_filtro = request.GET.get('categoria', '')
    mes_filtro = request.GET.get('mes', '')

    eventos = Evento.objects.all()
    if categoria_filtro:
        eventos = eventos.filter(categoria=categoria_filtro)
    if mes_filtro:
        eventos = eventos.filter(data_inicio__month=mes_filtro)

    # Meses disponíveis (sempre do total, para mostrar todos os botões)
    meses_disponiveis = (
        Evento.objects.values_list('data_inicio__month', flat=True)
        .distinct()
        .order_by('data_inicio__month')
    )
    meses = [{'num': m, 'nome': MESES_PT[m], 'abrev': MESES_PT[m][:3]} for m in meses_disponiveis]

    eventos_por_mes = []
    for mes_num, grupo in groupby(eventos, key=lambda e: e.data_inicio.month):
        eventos_por_mes.append({
            'mes': MESES_PT[mes_num],
            'mes_num': mes_num,
            'eventos': list(grupo),
        })

    return render(request, 'calendario/index.html', {
        'eventos_por_mes': eventos_por_mes,
        'categorias': Evento.CATEGORIA_CHOICES,
        'categoria_filtro': categoria_filtro,
        'mes_filtro': mes_filtro,
        'meses': meses,
        'total': eventos.count(),
    })
