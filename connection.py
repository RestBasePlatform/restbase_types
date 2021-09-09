class DatabaseConnectionData:
    host: str
    port: str
    username: str
    password: str
    connection_kwargs: dict

    def __init__(
        self, host: str, port: str, username: str, password: str, connection_kwargs: dict
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection_kwargs = connection_kwargs
