# Calendário Acadêmico Católica 2026

Aplicação web desenvolvida em Django para visualizar o calendário acadêmico da Católica (Palmas - TO) com feriados, recessos, eventos religiosos, institucionais e datas comemorativas do ano de 2026.

## Funcionalidades

- Listagem de eventos agrupados por mês
- Filtro por categoria e por mês
- Categorias com cores e ícones distintos:
  - Feriado
  - Recesso
  - Religioso
  - Social / Comemorativo
  - Semana de Mobilização
  - Evento Institucional
  - Outro
- Interface responsiva com filtros fixos no topo (sticky)
- Comando de gerenciamento para popular o banco de dados

## Tecnologias

- Python 3.12
- Django 6.0.3
- SQLite
- HTML/CSS puro (sem dependências de frontend)

## Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd feriado_catolica

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Popule o banco com os eventos de 2026
python manage.py popular_eventos

# Inicie o servidor
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000/`

## Estrutura do Projeto

```
feriado_catolica/
├── core/                   # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── calendario/             # App principal
│   ├── models.py           # Model Evento
│   ├── views.py            # View de listagem com filtros
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── calendario/
│   │       └── index.html
│   └── management/
│       └── commands/
│           └── popular_eventos.py  # Comando para popular o BD
├── manage.py
└── requirements.txt
```

## Comandos úteis

```bash
# Popular o banco de dados com os eventos de 2026
python manage.py popular_eventos

# Acessar o admin do Django
python manage.py createsuperuser
```
