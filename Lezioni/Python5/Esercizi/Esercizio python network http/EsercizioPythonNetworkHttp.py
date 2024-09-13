from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest, HTTPResponse
from datetime import datetime
import csv



iPkt: int = 0
with open("packet.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "IP Sorgente", "IP Destinatario", "TCP Sorgente", "TCP Destinatario", "Host"])        
    def process_pkt(pkt):
        global iPkt
        iPkt += 1
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        tcp_src = pkt[TCP].sport
        tcp_dst = pkt[TCP].dport
        if pkt.haslayer(HTTPRequest):
            host = pkt[HTTPRequest].Host
        else:
            host = "Unknown"
            writer.writerow([data, ip_src, ip_dst, tcp_src, tcp_dst, host])
        print(f"Pacchetto {iPkt}. Specifiche: data-ora: {data}, ip_src: {ip_src}, ip_dst: {ip_dst}, tcp_src: {tcp_src}, tcp_dst: {tcp_dst}, host: {host}")

    sniff(iface="eth0", filter="tcp", prn= process_pkt)