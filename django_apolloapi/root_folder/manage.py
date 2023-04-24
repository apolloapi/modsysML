#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

SYSTEM_ENV = os.environ.get("SYSTEM_ENV", None)


def main():
    """Run administrative tasks."""

    if SYSTEM_ENV == "PRODUCTION":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apolloapi.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apolloapi.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
