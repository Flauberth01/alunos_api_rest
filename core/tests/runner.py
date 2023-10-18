from types import MethodType

from django.conf import settings
from django.db import connections
from django.test.runner import DiscoverRunner


def prepare_data_with_schemas(self):
    self.connect()
    cursor = self.connection.cursor()
    for schema in settings.SCHEMAS:
        cursor.execute(f"""
        CREATE SCHEMA IF NOT EXISTS {schema};
        """)


class MyTestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs):
        for connection_name in connections:
            connection = connections[connection_name]
            connection.prepare_database = MethodType(prepare_data_with_schemas, connection)
        return super().setup_databases(**kwargs)
