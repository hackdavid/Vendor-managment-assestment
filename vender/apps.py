from django.apps import AppConfig

class VenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vender'

    def ready(self):
      import vender.signal
