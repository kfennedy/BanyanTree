from __future__ import unicode_literals

from django.apps import AppConfig


class BanyanAppConfig(AppConfig):
    name = 'BanyanApp'

    def ready(self):
        import BanyanApp.management.commands.arduino
