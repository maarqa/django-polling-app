import os
import sys

from django.core.management import execute_from_command_line

def run():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polling.settings')
      # Replace 'myproject' with your project's name
    
    try:
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])
    except Exception as errors:
        print(f"Error running server: {errors}")

if __name__ == "__main__":
    run()
