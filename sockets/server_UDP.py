"""
server_UDP.py

This file demonstrates a simple UDP server which accepts strings and returns
the string with all lowercase characters replaced by their uppercase
characters.

Usage:

    python server_UDP -A <IP Address of this server> -P <Port to listen on>
    
"""

import socket
import time
import argparse

BUFLEN = 2048

# Converts string argument to their uppercase representation
def convert(myStr):
    if(type(myStr) != str):
        return str(myStr).upper()
    return myStr.upper()

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-P', type=int, help='The desired port to listen on', required=True)
parser.add_argument('--address', '-A', type=str, help='The IP address of the remote server to connect to', required=True)

args = parser.parse_args()

PORT = args.port
IP_ADDR = args.address


try:
    # Set up connection, use internet protocol and datagrams (UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP_ADDR, PORT))

    while True:
        # Grab up to BUFLEN bytes from the connection
        payload, address = sock.recvfrom(BUFLEN)
        print("Received {} from host {}...".format(payload, address))

        if payload:
            # Send back the altered text
            # We can't use the same port we are listening on, since it will
            # create an endless loop.  Instead, we simply send it to the
            # address we received the message from, and let the other end
            # decide what to do with it.
            sock.sendto(convert(payload), address)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Handle intentional quit gracefully
    print("\n\nQuitting...")
