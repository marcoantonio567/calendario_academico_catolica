from django.core.management.base import BaseCommand
from django.db import transaction
from datetime import date
from calendario.models import Evento


EVENTOS = [
    # FERIADOS
    {'titulo': 'Confraternização Universal', 'data_inicio': date(2026, 1, 1), 'categoria': 'feriado'},
    {'titulo': 'Carnaval', 'data_inicio': date(2026, 2, 17), 'categoria': 'feriado'},
    {'titulo': 'São José (Padroeiro de Palmas)', 'data_inicio': date(2026, 3, 19), 'categoria': 'feriado'},
    {'titulo': 'Paixão de Cristo', 'data_inicio': date(2026, 4, 3), 'categoria': 'feriado'},
    {'titulo': 'Tiradentes', 'data_inicio': date(2026, 4, 21), 'categoria': 'feriado'},
    {'titulo': 'Dia do Trabalho', 'data_inicio': date(2026, 5, 1), 'categoria': 'feriado'},
    {'titulo': 'Aniversário de Palmas', 'data_inicio': date(2026, 5, 20), 'categoria': 'feriado'},

    # RECESSOS
    {'titulo': 'Recesso Carnaval', 'data_inicio': date(2026, 2, 16), 'categoria': 'recesso'},
    {'titulo': 'Quarta-feira de Cinzas', 'data_inicio': date(2026, 2, 18), 'categoria': 'recesso'},
    {'titulo': 'Autonomia do Tocantins', 'data_inicio': date(2026, 3, 18), 'categoria': 'recesso'},
    {'titulo': 'Quinta-feira Santa', 'data_inicio': date(2026, 4, 2), 'categoria': 'recesso'},
    {'titulo': 'Sábado Santo', 'data_inicio': date(2026, 4, 4), 'categoria': 'recesso'},
    {'titulo': 'Corpus Christi', 'data_inicio': date(2026, 6, 4), 'categoria': 'recesso'},
    {'titulo': 'Recesso Docente', 'data_inicio': date(2026, 7, 6), 'data_fim': date(2026, 7, 12), 'categoria': 'recesso'},

    # RELIGIOSOS
    {'titulo': 'São João Bosco', 'data_inicio': date(2026, 1, 31), 'categoria': 'religioso'},
    {'titulo': 'Início da Quaresma / Campanha da Fraternidade', 'data_inicio': date(2026, 2, 18), 'categoria': 'religioso'},
    {'titulo': 'Domingo de Ramos', 'data_inicio': date(2026, 3, 29), 'categoria': 'religioso'},
    {'titulo': 'Páscoa', 'data_inicio': date(2026, 4, 5), 'categoria': 'religioso'},
    {'titulo': 'São João Batista de La Salle', 'data_inicio': date(2026, 4, 7), 'categoria': 'religioso'},
    {'titulo': 'Santa Maria Mazzarello', 'data_inicio': date(2026, 5, 13), 'categoria': 'religioso'},
    {'titulo': 'São Marcelino Champagnat', 'data_inicio': date(2026, 6, 6), 'categoria': 'religioso'},
    {'titulo': 'São Gaspar Bertoni', 'data_inicio': date(2026, 6, 12), 'categoria': 'religioso'},

    # SOCIAIS / COMEMORATIVOS
    {'titulo': 'Janeiro Branco', 'data_inicio': date(2026, 1, 2), 'data_fim': date(2026, 1, 30), 'categoria': 'social'},
    {'titulo': 'Dia Mundial da Água', 'data_inicio': date(2026, 3, 22), 'categoria': 'social'},
    {'titulo': 'Dia dos Povos Indígenas', 'data_inicio': date(2026, 4, 19), 'categoria': 'social'},
    {'titulo': 'International Day', 'data_inicio': date(2026, 4, 27), 'categoria': 'social'},
    {'titulo': 'Festa Junina', 'data_inicio': date(2026, 6, 12), 'categoria': 'social'},

    # SEMANAS DE MOBILIZAÇÃO
    {'titulo': 'Semana de Combate ao Bullying', 'data_inicio': date(2026, 4, 6), 'data_fim': date(2026, 4, 11), 'categoria': 'mobilizacao'},
    {'titulo': 'Semana de Combate ao Abuso e Exploração Sexual', 'data_inicio': date(2026, 5, 18), 'data_fim': date(2026, 5, 23), 'categoria': 'mobilizacao'},
    {'titulo': 'Semana do Meio Ambiente', 'data_inicio': date(2026, 6, 1), 'data_fim': date(2026, 6, 6), 'categoria': 'mobilizacao'},

    # EVENTOS INSTITUCIONAIS
    {'titulo': 'Planejamento Docente', 'data_inicio': date(2026, 1, 26), 'data_fim': date(2026, 2, 6), 'categoria': 'institucional'},
    {'titulo': 'Início das Aulas', 'data_inicio': date(2026, 2, 9), 'categoria': 'institucional'},
    {'titulo': 'Aula Magna', 'data_inicio': date(2026, 3, 2), 'categoria': 'institucional'},
    {'titulo': 'Acolhida dos Cursos', 'data_inicio': date(2026, 3, 3), 'categoria': 'institucional'},
    {'titulo': 'Semana da Mulher', 'data_inicio': date(2026, 3, 9), 'data_fim': date(2026, 3, 14), 'categoria': 'institucional'},
    {'titulo': 'Semana Acadêmica', 'data_inicio': date(2026, 5, 25), 'data_fim': date(2026, 5, 30), 'categoria': 'institucional'},
    {'titulo': 'Intercatólica', 'data_inicio': date(2026, 5, 28), 'data_fim': date(2026, 5, 30), 'categoria': 'institucional'},
    {'titulo': 'Última Avaliação', 'data_inicio': date(2026, 6, 27), 'categoria': 'institucional'},
    {'titulo': 'Último Dia Letivo', 'data_inicio': date(2026, 7, 4), 'categoria': 'institucional'},

    # OUTROS
    {'titulo': 'Exames Finais', 'data_inicio': date(2026, 6, 29), 'data_fim': date(2026, 7, 4), 'categoria': 'outro'},
    {'titulo': 'Revisão de Notas', 'data_inicio': date(2026, 7, 6), 'data_fim': date(2026, 7, 11), 'categoria': 'outro'},
]


class Command(BaseCommand):
    help = 'Popula o banco de dados com os eventos do calendário acadêmico da Católica 2026'

    def handle(self, *args, **options):
        with transaction.atomic():
            Evento.objects.all().delete()
            criados = 0
            for dados in EVENTOS:
                Evento.objects.create(**dados)
                criados += 1
            self.stdout.write(self.style.SUCCESS(f'{criados} eventos criados com sucesso!'))
