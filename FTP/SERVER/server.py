from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():

    authorizer = DummyAuthorizer()

    authorizer.add_user(
        "user",
        "12345",
        "/home/ubuntu/Desktop/Dev/Network/FTP/server",
        perm="elradfmMT"
    )

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 2121), handler)

    print("FTP Server running on port 2121...")
    print("Username: user")
    print("Password: 12345")

    server.serve_forever()


if __name__ == "__main__":
    main()
