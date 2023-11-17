import socket

def port_scan(target_host, target_ports):
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"Scanning target {target_ip}")

        for target_port in target_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, target_port))
            if result == 0:
                print(f"Port {target_port} is open")
            else:
                print(f"Port {target_port} is closed")
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
    except socket.error:
        print("Couldn't connect to the server.")

target_host = "192.168.1.1"  
# target_ports = range(125,135)
target_ports = 22,80,433

port_scan(target_host, target_ports)