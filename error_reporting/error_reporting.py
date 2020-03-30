from scapy.all import *
from os import system

pcap = rdpcap("error_reporting.pcap")

data = [p.load for p in pcap if p[IP].src == "192.168.10.113"]

bytes = b"".join(data)

with open("flag.jpg", "wb") as f:
    f.write(bytes)

system("eog flag.jpg")
