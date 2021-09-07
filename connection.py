class DatabaseConnectionData:
    host: str
    port: str
    username: str
    password: str
    con_kwargs: dict

    def __init__(
        self, host: str, port: str, username: str, password: str, con_kwargs: dict
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.con_kwargs = con_kwargs
