#!/usr/bin/env python
dj4e_user1 / Meow_f8ee6a_41  
dj4e_user2 / Meow_42_f8ee6a 
<meta name="dj4e" content="ff8ee6aac61c11f16443646cdf467146">
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj4e.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
