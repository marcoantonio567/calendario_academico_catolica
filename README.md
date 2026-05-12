````md
# Católica Academic Calendar 2026

Web application developed with Django to display the academic calendar of Católica (Palmas - TO, Brazil), including holidays, breaks, religious events, institutional events, and commemorative dates for the year 2026.

## Features

- Event listing grouped by month
- Filtering by category and month
- Categories with distinct colors and icons:
  - Holiday
  - Break
  - Religious
  - Social / Commemorative
  - Mobilization Week
  - Institutional Event
  - Other
- Responsive interface with sticky filters at the top
- Management command to populate the database

## Technologies

- Python 3.12
- Django 6.0.3
- SQLite
- Pure HTML/CSS (no frontend dependencies)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd feriado_catolica

# Create and activate the virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Populate the database with 2026 events
python manage.py popular_eventos

# Start the server
python manage.py runserver
````

Access at `http://127.0.0.1:8000/`

## Project Structure

```text
feriado_catolica/
├── core/                   # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── calendario/             # Main application
│   ├── models.py           # Event model
│   ├── views.py            # List view with filters
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── calendario/
│   │       └── index.html
│   └── management/
│       └── commands/
│           └── popular_eventos.py  # Command to populate the database
├── manage.py
└── requirements.txt
```

## Useful Commands

```bash
# Populate the database with 2026 events
python manage.py popular_eventos

# Access the Django admin panel
python manage.py createsuperuser
```
