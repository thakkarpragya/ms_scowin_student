from django.apps import AppConfig
from health_check.plugins import plugin_dir

class HealthChecksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_checks'

    def ready(self):
        from health_checks.health_checks import MyHealthCheckBackend
        # from health_checks.views import HealthCheckCustomView

        plugin_dir.register(MyHealthCheckBackend)
        # plugin_dir.register(HealthCheckCustomView)