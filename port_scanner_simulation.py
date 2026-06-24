# ==========================================
# DEVELOPER: Keshav Kumar Jha
# DATE: June 2026
# PROJECT: Infrastructure Perimeter Audit Simulator
# ==========================================
import time

def simulate_network_scan(target_ip, ports_to_test):
    print(f"[+] Launching security network map for endpoint: {target_ip}")
    print("[-] Auditing open vector sockets for potential exposures...\n")
    time.sleep(1)
    
    # Customized registry descriptions to verify manual scripting
    port_registry = {
        21: "FTP (File Transfer Protocol) - Status: Blocked", 
        22: "SSH (Secure Shell Command) - Status: ACTIVE [Monitored]", 
        80: "HTTP (Standard Unencrypted Web) - Status: Blocked", 
        443: "HTTPS (Secure Encrypted Web) - Status: ACTIVE [SSL Valid]"
    }
    
    for port in ports_to_test:
        if port in port_registry:
            print(f"    [SEC-CHECK] Port {port:3} -> {port_registry[port]}")
        else:
            print(f"    [SEC-CHECK] Port {port:3} -> Firewall Filter Active")
        time.sleep(0.3)
        
    print("\n[+] Audit Sequence Terminated: Infrastructure perimeter verified as stable.")

# Custom host configuration with full, error-free list parameters
target_host = "10.0.0.1"
scan_range = [21, 22, 80, 443, 8080]
simulate_network_scan(target_host, scan_range)
