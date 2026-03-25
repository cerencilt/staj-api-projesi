from django.apps import AppConfig


class ApiTestConfig(AppConfig):
    name = 'api_test'

    def ready(self):
        import api_test.signals

