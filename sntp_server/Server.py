import argparse
import collections
import concurrent.futures as cf
import socket
from threading import Thread

import Parser


queue = collections.deque()


class Server:
    def __init__(self,inaccuracy):
        self.inaccuracy = inaccuracy
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.5)
        self.sock.bind(("", 123))

    def read(self):
        while True:
            try:
               data, addr = self.sock.recvfrom(1024)
            except socket.timeout:
                continue
            fields = Parser.parse_from(data)
            queue.append((fields, addr))

    def logic(self, connection):
        fields, addr = connection
        packet = Parser.parse_to(self.inaccuracy, fields)
        with socket.socket(type=socket.SOCK_DGRAM) as reply_socket:
            try:
                reply_socket.sendto(packet, addr)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-shift", "--inaccuracy", action="store", type=int, default=0)
    args = parser.parse_args()
    s = Server(args.inaccuracy)
    receive = Thread(target=s.read)
    try:
        receive.start()
        with cf.ThreadPoolExecutor(max_workers=5) as executor:
            while True:
                if queue:
                    executor.submit(s.logic,queue.popleft())
    except KeyboardInterrupt:
        print("Shut off")
        receive.join(1)
        s.sock.close()
    except Exception:
        print("Something went wrong")