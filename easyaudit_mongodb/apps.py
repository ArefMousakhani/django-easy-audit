from django.apps import AppConfig

class EasyAuditConfig(AppConfig):
    name = 'easyaudit_mongodb'
    verbose_name = 'Easy Audit Application'

    def ready(self):
        from easyaudit_mongodb.signals import auth_signals, model_signals, request_signals