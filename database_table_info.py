from typing import List


class DatabaseColumn:
    def __init__(self, name: str, data_type):
        self.name = name
        self.data_type = data_type

    name: str
    data_type: str


class DatabaseSchema:
    name: str

    def __init__(self, name: str):
        self.name = name


class Database:
    name: str

    def __init__(self, name: str):
        self.name = name


class DatabaseTable:
    def __init__(
        self,
        name: str,
        schema: DatabaseSchema,
        database: Database,
        column_list: List[DatabaseColumn],
    ):
        self.name = name
        self.schema = schema
        self.database = database
        self.column_list = column_list

    database: Database
    schema: DatabaseSchema
    name: str
    column_list: List[DatabaseColumn]
