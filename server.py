class ServerConnectionCredentials:
    username: str
    ssh_key: str
    password: str

    def __init__(
            self,
            username: str,
            ssh_key: str,
            password: str,
    ):
        self.username = username
        self.password = password
        self.ssh_key = ssh_key


class ServerConnectionData:
    host: str
    port: int
    connection_kwargs: dict
    connection_data: ServerConnectionCredentials

    def __init__(
            self,
            host: str,
            port: int,
            connection_kwargs: dict,
            connection_data: ServerConnectionCredentials
    ):
        self.host = host
        self.port = port
        self.connection_kwargs = connection_kwargs
        self.connection_data = connection_data
