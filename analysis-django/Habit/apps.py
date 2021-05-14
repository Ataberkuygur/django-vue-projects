from django.apps import AppConfig


class HabitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Habit'

    def ready(self):
        from .signals import create_days
