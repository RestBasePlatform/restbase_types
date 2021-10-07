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
