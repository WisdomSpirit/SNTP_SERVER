import argparse
import concurrent.futures as cf
import Interaction
import Parser


class Server:
    def __init__(self,inaccuracy):
        self.inaccuracy = inaccuracy

    def logic(self):
        self._connection = Interaction.Interaction()
        data = self._connection.recieve_data()
        fields = Parser.parse_from(data)
        packet = Parser.parse_to(self.inaccuracy, fields)
        self._connection.send_data(packet)
        self._connection.close()

    def close(self):
        self._connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-shift", "--inaccuracy", action="store", type=int, default=0)
    args = parser.parse_args()
    try:
        with cf.ThreadPoolExecutor(max_workers=5) as executor:
            while True:
                s = Server(args.inaccuracy)
                s.logic()
    except KeyboardInterrupt:
        print("Shut off")
        s.close()
    except Exception:
        print("Something went wrong")