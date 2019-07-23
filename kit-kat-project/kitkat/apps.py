from django.apps import AppConfig


class KitkatConfig(AppConfig):
    name = 'kitkat'

    def ready(self):
        import kitkat.signals
