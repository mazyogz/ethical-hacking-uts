import nmap

target = "192.168.1.1"

scanner = nmap.PortScanner()
scanner.scan(target, ports= "22, 80, 443")

for host in scanner.all_hosts():
    for port in scanner[host]['tcp']:
        print (host, port, scanner[host]['tcp'][port]['state'])