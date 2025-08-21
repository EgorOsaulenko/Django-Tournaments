import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TournamentX.settings')
django.setup()

from tournaments.models import User

username = "admin"
email = "admin@email.com"
password = "12345"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Суперюзер {username} створен!")
else:
    print(f"Суперюзер {username} вже є.")