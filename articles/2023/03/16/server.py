import socket
import threading







def main() -> None:
    print(f'Hello main from : {__file__}')
    host = ''
    port = 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"Received connection {conn=} :: {addr=}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data.upper())


if __name__ == '__main__':
    main()