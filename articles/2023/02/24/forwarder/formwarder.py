import sys
import socket
import select
from logzero import logger

from pprint import pprint

class Forwarder:
    def __init__(self, src_ip, src_port, dst_ip, dst_port) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        logger.info(f"Binding to {src_ip}:{src_port}")
        self.sock.bind((src_ip, src_port))
        self.sock.listen(5)
        self.target = (dst_ip, dst_port)

    def coding(self, data):
        return data

    def exchange_loop(self, client, remote):
        while True:
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                data = client.recv(4096)
                logger.debug(f" CLIENT > REMOTE : {len(data)} bytes")
                pprint(self.coding(data))
                if remote.send(self.coding(data)) <= 0:
                    return

            if remote in r:
                data = remote.recv(4096)
                logger.debug(f" CLIENT < REMOTE : {len(data)} bytes")
                pprint(self.coding(data))
                if client.send(self.coding(data)) <= 0:
                    return


    def run(self):
        remote = None
        try:
            while True:
                client, addr = self.sock.accept()
                logger.info(f"[NEW] CLIENT({addr}) forward REMOTE({self.target}) ")

                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect(self.target)

                self.exchange_loop(client, remote)

                client.close()
                logger.info(f"[CLOSE] CLIENT({addr[0]})")

        except Exception as e:
            logger.error(e)
        finally:
            if remote is not None:
                remote.close()
            logger.info(f"[CLOSE] REMOTE({self.target[0]})")


class SecureForwarderXD(Forwarder):

    def xor(self, data, key_byte=42):
        result = b""
        for b in data:
            result += bytes([b ^ key_byte])
        return result

    def coding(self, data):
        return self.xor(data)



def main() -> None:
    print(f"Hello main from : {__file__}")

    src_ip, src_port = sys.argv[1].split(":")
    src_port = int(src_port)
    dst_ip, dst_port = sys.argv[2].split(":")
    dst_port = int(dst_port)

    logger.info(f"TCP Forward {src_ip}:{src_port} ===> {dst_ip}:{dst_port}")
    if len(sys.argv) > 3 and sys.argv[3] == "secure":
        logger.info("Creation of \"SECURE\" forwarder")
        proxy = SecureForwarderXD(src_ip, src_port, dst_ip, dst_port)
    else:
        logger.info("Creation of NORMAL forwarder")
        proxy = Forwarder(src_ip, src_port, dst_ip, dst_port)
    proxy.run()

if __name__ == "__main__":
    main()