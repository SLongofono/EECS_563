"""
client_TCP.py

This file demonstrates a simple TCP client which sends data to a remote server
and gathers the reply.

Usage:

    python client_TCP.py --help
    
"""

import socket
import argparse

# Trims input to expected maximum size
def trim(myStr):
    if len(myStr) > 2048:
        print("Your input was larger than the maximum of {} bytes and has"
              "been truncated to fit.".format(BUFLEN))
        return myStr[:2048-len(myStr)]
    return myStr

# Per instructions, "print the address and port using a function"
def print_address_port(a,b):
    print("\tIP Address {}\n\tPort {}\n".format(a,b))

BUFLEN = 2048

parser = argparse.ArgumentParser()
parser.add_argument('--port',
                    '-P',
                    type=int,
                    help='The desired port on the remote server',
                    required=True)
parser.add_argument('--address',
                    '-A',
                    type=str,
                    help='The IP address of the remote server to connect to',
                    required=True)

args = parser.parse_args()

PORT = args.port
SERVER_ADDR = args.address

print("Attempting to connect to IP address {}"
      "on port {}...".format(SERVER_ADDR, PORT))

try:
    sock = None

    # Set up connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_ADDR, PORT))

    print("Connection established to IP address {}".format(SERVER_ADDR))
    print("Press Ctrl-C to quit")

    while True:
        
        raw = raw_input("Please enter the statement: ")

        # Send the user's input through the socket TCP connection
        sock.send(trim(raw))

        print("Local details:\n")
        localaddress, localport = sock.getsockname()
        print_address_port(localaddress, localport)

        # Grab up to BUFLEN bytes from the connection reply
        payload = sock.recv(BUFLEN)
        if payload:
            print("Return text from the server: {}".format(payload))
            print("Remote details:\n")
            print_address_port(SERVER_ADDR, PORT)
            

except KeyboardInterrupt:
    # Handle intentional quit gracefully
    print("\n\nQuitting...")

finally:
    # Tear-down connection
    if sock is not None:
        sock.close()
