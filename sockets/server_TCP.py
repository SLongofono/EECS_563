"""
server_TCP.py

This file demonstrates a simple TCP server which accepts strings and returns
the string with all lowercase characters replaced by their uppercase
characters.

Usage:

    python server_TCP.py -P <Port to listen on>
    
"""

import socket
import argparse

# Converts string argument to their uppercase representation
def convert(myStr):
    if(type(myStr) != str):
        raise RuntimeException('Cannot convert non-string input to lower case.  Please pass in a string')
    return myStr.upper()

# Per instructions, "print the address and port using a function"
def print_address_port(a,b):
    print("\tIP Address {}\n\tPort {}\n".format(a,b))

IP_ADDR = '127.0.0.1' # Use localhost
BUFLEN = 2048

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-P', type=int, help='The desired port for socket communication', required=True)
args = parser.parse_args()

PORT = args.port

print("Listening at IP address {} on port {}...".format(IP_ADDR, PORT))

try:
    # Set up connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP_ADDR, PORT))
    sock.listen(1) # listen for a maximum of 1 connections

    # If we got this far, we found someone trying to connect.  Accept the
    # connection and gather the connection object and its IP address.
    connection, client_address = sock.accept()


    print("Connection established to IP address {}".format(client_address))
    print("Local details:\n")
    localaddr, localport = connection.getsockname()
    print_address_port(localaddr, localport)

    while True:
        # Grab up to BUFLEN bytes from the connection
        payload = connection.recv(BUFLEN)
        if payload:
            print("Received text from client: {}".format(payload))
            print("Remote details:\n")
            print_address_port(client_address[0], client_address[1])

            # Send back the altered text
            connection.send(convert(payload))

except KeyboardInterrupt:
    # Handle intentional quit gracefully
    print("\n\nQuitting...")

finally:
    # Tear-down connection
    if connection is not None:
        connection.close()
