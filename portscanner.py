import socket  # Used for low-level networking (e.g., opening TCP connections)
import argparse  # For parsing command-line arguments

# Function to scan a single port on a given IP
def scan_port(ip, port):
    try:
        # Create a socket object (default: IPv4, TCP)
        sock = socket.socket()
        
        # Set a timeout so the scan doesn't hang on closed/filtered ports
        sock.settimeout(1)
        
        # Try to connect to the specified IP and port
        sock.connect((ip, port))
        
        # If connection is successful, the port is open
        print(f"[+] Port {port} is open")
    
    except:
        # If connection fails, just pass (port is closed or filtered)
        pass
    
    finally:
        # Close the socket connection after each attempt
        sock.close()

# Main function that handles input and logic
def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    
    # Add required argument: target host (domain or IP)
    parser.add_argument("host", help="Target host to scan")
    
    # Add optional argument: ports to scan (default is 1–1024)
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g. 22,80,443 or 1-1024)", default="1-1024")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert hostname to IP address
    target_ip = socket.gethostbyname(args.host)
    print(f"Scanning {args.host} ({target_ip})...")

    ports = []

    # If a port range is provided (e.g. 1-100)
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    
    # If a comma-separated list of ports is provided (e.g. 22,80,443)
    else:
        ports = [int(p.strip()) for p in args.ports.split(",")]

    # Loop through each port and scan it
    for port in ports:
        scan_port(target_ip, port)

# Entry point of the script
if __name__ == "__main__":
    main()
