from scapy.all import sniff
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest, HTTPResponse
from datetime import datetime
iPkt: int = 0
def process_pkt(pkt):
    global iPkt
    iPkt += 1
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_src = pkt[IP].src
    ip_dst = pkt[IP].dst
    tcp_src = pkt[IP].sport
    tcp_dst = pkt[IP].dport
    host = 0
    
    with open("packet.csv", "a") as file:
        file.write(f"Numero: {iPkt}, Data: {data}, Ip_src: {ip_src}, Ip_dst: {ip_dst}, Tcp_src: {tcp_src}, Tcp_dst: {tcp_dst}, Host: {host}\n")
    print(f"Pacchetto {iPkt}. Specifiche: data-ora: {data}, ip_src: {ip_src}, ip_dst: {ip_dst}, tcp_src: {tcp_src}, tcp_dst: {tcp_dst}, host: {host}")

sniff(iface="eth0", filter="tcp", prn= process_pkt)