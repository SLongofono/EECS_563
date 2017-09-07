import socket
import argparse

IP_ADDR = '127.0.0.1' # Use localhost
BUFLEN = 2048

# Converts string argument to their uppercase representation
def convert(myStr):
    if(type(myStr) != str):
        raise RuntimeException('Cannot convert non-string input to lower case.  Please pass in a string')
    return myStr.upper()

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-P', type=int, help='The desired port for socket communication', required=True)
args = parser.parse_args()

PORT = args.port

print("The port passed in was {}".format(PORT))
print("Listening at IP address {} on port {}...".format(IP_ADDR, PORT))

try:
    # Set up connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP_ADDR, PORT))
    sock.listen(1) # listen for a maximum of 1 connections

    # If we got this far, we found someone trying to connect.  Accept the
    # connection and gather the connection object and its IP address.
    connection, address = sock.accept()


    print("Connection established to IP address {}".format(address))
    while True:
        # Grab up to BUFLEN bytes from the connection
        payload = connection.recv(BUFLEN)
        if payload:
            # Send back the altered text
            connection.send(convert(payload))

except KeyboardInterrupt:
    # Handle intentional quit gracefully
    print("\n\nQuitting...")

finally:
    # Tear-down connection
    if None != connection:
        connection.close()
