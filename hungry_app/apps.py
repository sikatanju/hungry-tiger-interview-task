from django.apps import AppConfig


class HungryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hungry_app'

    def ready(self):
        import hungry_app.signals
