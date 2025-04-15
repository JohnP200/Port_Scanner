import socket

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            sock.close()

# Example usage
if __name__ == "__main__":
    target = input("Enter the target IP address or hostname to scan:")
    ports = [22, 23, 21, 25, 53, 80, 110, 143, 443, 445, 3306,8080]
    scan_ports(target, ports_to_scan)