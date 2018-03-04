import socket


class Interaction:
    def __init__(self):
        """initialize connection"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(1)
        self.sock.bind(("", 123))

    def recieve_data(self):
        """Read data from client with a buffer of 1024 bytes and send him our data"""
        try:
            while True:
                try:
                    data, self.addr = self.sock.recvfrom(1024)
                    return data
                except socket.timeout:
                    print("There is no packet at all!")
                    break
        except Exception:
            print("Can't recieve a package")

    def send_data(self, data):
        """Send Your data to the client"""
        try:
            self.sock.sendto(data, self.addr)
        except Exception:
            print("Cant't send a package")

    def close(self):
        """Close connection"""
        self.sock.close()