import socket
import os



def main() -> None:
    print(f'Hello main from : {__file__}')
    print(socket.gethostname())
    print(socket.gethostbyname(socket.gethostname()))
    print(socket.getfqdn())

if __name__ == '__main__':
    main()