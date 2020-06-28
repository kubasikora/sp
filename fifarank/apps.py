from django.apps import AppConfig

class FifarankConfig(AppConfig):
    name = 'fifarank'

    def ready(self):
        import fifarank.signals