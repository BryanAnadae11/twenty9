from django.apps import AppConfig


class Twenty9WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twenty9webapp'

    def ready(self):
    	import twenty9webapp.signals
