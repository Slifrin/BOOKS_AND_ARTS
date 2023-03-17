import socket


def main() -> None:
    print(f'Hello main from : {__file__}')
    host = 'epplgdaw0265.home'
    port = 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello there")
        data = s.recv(1024)
        print(f"Received {data=}")

if __name__ == '__main__':
    main()