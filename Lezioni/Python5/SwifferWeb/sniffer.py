from scapy.all import *
from scapy.layers.http import HTTPRequest, HTTPResponse

sniff(ifaces="eth5", filter="tcp", prn= process_pkt)