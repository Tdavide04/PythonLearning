from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.tls.record import TLS
from scapy.layers.http import HTTPRequest, HTTPResponse
from datetime import datetime
import csv


def get_tls_sni(pkt):
    try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
    except (IndexError, AttributeError):
        return ""


def process_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]:

            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip_src = pkt[IP].src
            ip_dst = pkt[IP].dst
            tcp_src = pkt[TCP].sport
            tcp_dst = pkt[TCP].dport

            host = ""
            if HTTPRequest in pkt:
                if pkt[HTTPRequest].Host:
                    host = pkt[HTTPRequest].Host.decode()
            elif TLS in pkt:
                host = get_tls_sni(pkt)

            if 443 in [tcp_src, tcp_dst]:
                protocol = "HTTPS"
            else:
                protocol = "HTTP"
                
            with open("packet.csv", "a", newline="") as file:
                writer = csv.writer(file)
                if host != "":
                    writer.writerow([data, ip_src, ip_dst, tcp_src, tcp_dst, host, protocol])

with open("packet.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "IP Sorgente", "IP Destinatario", "TCP Sorgente", "TCP Destinatario", "Host", "Protocol"])        

sniff(iface="eth0", filter="tcp", prn= process_pkt)