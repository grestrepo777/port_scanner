import socket, sys

try: 
    target = input("Enter IP to scan: ")
    print(f"\nScanning {target} from port 20 to port 1023\n")

    for port in range (20, 1024):  # port range 20 - 1023
        openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket object (IPv4, TCP)
        openSocket.settimeout(0.2) # give it some time to wait for a response
        result = openSocket.connect_ex((target, port))  # Returns a value based on whether a port is open or closed
        if result == 0: # 0 = open port, any other value = closed port
            print(f"Port {port} is open")
        openSocket.close() # close the socket/end connection

except KeyboardInterrupt:  # ctrl + c to end the scan
    print("Scanning cancelled")

    sys.exit()

