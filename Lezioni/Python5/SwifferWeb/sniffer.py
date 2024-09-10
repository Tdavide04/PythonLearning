from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest, HTTPResponse

iPkt: int = 0
def process_pkt(pkt):
    iPkt += 1
    print(f"Ho ricevuto un pacchetto {iPkt} lungo {pkt[IP].len}")

sniff(ifaces="eth0", filter="tcp", prn= process_pkt)