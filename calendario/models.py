from django.db import models


class Evento(models.Model):
    CATEGORIA_CHOICES = [
        ('feriado', 'Feriado'),
        ('recesso', 'Recesso'),
        ('religioso', 'Religioso'),
        ('social', 'Social / Comemorativo'),
        ('mobilizacao', 'Semana de Mobilização'),
        ('institucional', 'Evento Institucional'),
        ('outro', 'Outro'),
    ]

    CORES = {
        'feriado': '#ef4444',
        'recesso': '#f97316',
        'religioso': '#3b82f6',
        'social': '#22c55e',
        'mobilizacao': '#eab308',
        'institucional': '#a855f7',
        'outro': '#6b7280',
    }

    ICONES = {
        'feriado': '🔴',
        'recesso': '🟠',
        'religioso': '🔵',
        'social': '🟢',
        'mobilizacao': '🟡',
        'institucional': '🟣',
        'outro': '📌',
    }

    titulo = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ['data_inicio']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo

    @property
    def cor(self):
        return self.CORES.get(self.categoria, '#6b7280')

    @property
    def icone(self):
        return self.ICONES.get(self.categoria, '📌')

    @property
    def e_multiplos_dias(self):
        return self.data_fim is not None and self.data_fim != self.data_inicio

    @property
    def data_exibicao(self):
        if self.e_multiplos_dias:
            return f"{self.data_inicio.strftime('%d/%m')} a {self.data_fim.strftime('%d/%m')}"
        return self.data_inicio.strftime('%d/%m')

    @property
    def dia_semana(self):
        DIAS_PT = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        return DIAS_PT[self.data_inicio.weekday()]
