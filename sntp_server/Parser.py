import random
import struct

import Time

ID = [10,113,241,246]

def parse_from(data):
    """Parse the SNTP UDP packet"""
    try:
        packet = struct.unpack(b"!BBBbiI4B2I2I2I2I", data[:48])
        result = []
        LI = int(bin(packet[0])[2:4], 2)
        VN = int(bin(packet[0])[4:7], 2)
        MODE = int(bin(packet[0])[7:10], 2)
        STRATUM = packet[1]
        Poll = packet[2]
        Precision = packet[3]
        Root_Delay =packet[4]
        Root_Dispersion = packet[5]
        Reference_Identifier = packet[6:10]
        Reference_Timestamp = packet[10:12]
        Originate_Timestamp = packet[12:14]
        Receive_Timestamp = packet[14:16]
        Transmit_Timestamp = packet[16:18]
        return (LI, VN, MODE, STRATUM, Poll, Precision, Root_Delay, Root_Dispersion, Reference_Identifier,
                Reference_Timestamp, Originate_Timestamp, Receive_Timestamp, Transmit_Timestamp)
    except Exception:
        print("Cant parse a package, is it the right one?")

def parse_to(inaccuracy, args):
    """Create a SNTP packet with modified fields (time and flags)"""
    try:
        li = args[0]
        version = 4
        mode = 4
        LIVNMODE = (li << 6) + (version << 3) + mode
        stratum = 3
        poll = args[4]
        precision = random.randint(-20,-6)
        root_delay = random.randint(0, 512)
        root_disp = random.randint(0, 512)
        reference_identifier = 0
        shifter = 24
        i = 0
        while shifter != 0:
            reference_identifier += ID[i] << shifter
            shifter -= 8
            i += 1
        time = Time.get_time(inaccuracy)
        reference_timestamp = time << 32 + random.randint()
        originate_timestamp = args[12]
        recieved_timestamp = time << 32 + random.randint()
        transmit_timestamp = time << 32 + random.randint()

        return struct.pack("!BBBbiI4B2I2I2I2I",
                           (LIVNMODE, stratum, poll, precision, root_delay, root_disp, reference_identifier +
                                          reference_timestamp, originate_timestamp, recieved_timestamp, transmit_timestamp))
    except Exception:
        print("Can't make a package from a data, recieved")