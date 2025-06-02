import socket
import argparse

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is open")
    except:
        pass
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g. 22,80,443 or 1-1024)", default="1-1024")
    args = parser.parse_args()

    target_ip = socket.gethostbyname(args.host)
    print(f"Scanning {args.host} ({target_ip})...")

    ports = []
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(p.strip()) for p in args.ports.split(",")]

    for port in ports:
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()
