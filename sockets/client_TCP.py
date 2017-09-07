import socket
import argparse

# Trims input to expected maximum size
def trim(myStr):
    if len(myStr) > 2048:
        print("Your input was larger than the maximum of {} bytes and has been truncated to fit.".format(BUFLEN))
        return myStr[:2048-len(myStr)]
    return myStr

BUFLEN = 2048

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-P', type=int, help='The desired port for socket communication', required=True)
parser.add_argument('--address', '-A', type=str, help='The IP address of the remote server to connect to', required=True)

args = parser.parse_args()

PORT = args.port
SERVER_ADDR = args.address

print("The port passed in was {}".format(PORT))
print("Attempting to connect to IP address {} on port {}...".format(SERVER_ADDR, PORT))

try:
    # Set up connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_ADDR, PORT))

    print("Connection established to IP address {}".format(SERVER_ADDR))
    print("Press Ctrl-C to quit")

    while True:
        
        raw = raw_input("Please enter the statement: ")

        # Send the user's input through the socket TCP connection
        sock.send(trim(raw))
        
        # Grab up to BUFLEN bytes from the connection reply
        payload = sock.recv(BUFLEN)
        if payload:
            print("Return text from the server: {}".format(payload))

except KeyboardInterrupt:
    # Handle intentional quit gracefully
    print("\n\nQuitting...")

finally:
    # Tear-down connection
    if None != sock:
        sock.close()
