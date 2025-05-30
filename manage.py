#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # adapte 'config.settings' selon ton projet
    
    import django
    from django.core.management import execute_from_command_line
    
    django.setup()
    
    from django.core.management import call_command
    # Lancer les migrations automatiquement
    call_command('migrate', interactive=False)
    
    # Création du superuser automatique si aucun n'existe
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        print("Création automatique du superuser: admin/admin123")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()







# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
