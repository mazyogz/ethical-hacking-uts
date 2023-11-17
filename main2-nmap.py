import nmap

def nmap_scan(target_host, target_ports):
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=target_host, ports=target_ports)

    for host in nm.all_hosts():
        print(f"Scanning target {host}")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                print(f"Port {port} is {state}")

# Example usage:
target_host = "192.168.1.1"  # Ganti dengan hostname atau IP address target
# target_ports = range(125,135)
target_ports = "22,80,433"

nmap_scan(target_host, target_ports)