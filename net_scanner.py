import subprocess

def scan_network(base_ip):
    print(f"[*] starting network scan on {base_ip}.x ...")
    print("[*] This will take a moment. Pinging 254 addresses...\n")
          
          
    active_devices = 0
    
    # 1. The loop: count from 1 to 254
    for i in range(1,255):
        # 2. STring Formatting: combine the base IP with the current number 
        target_ip = f"{base_ip}.{i}]"
        
        # 3. The linux command : ping -c 1 -W 1 <ip>
        # -c 1 : Send exactly 1 ping packet
        # -W 1 : Wait exactly 1 secaond for response prevents it from hanging forever)
        ping_cmd = ["ping", "-c", "1", "-W", "1", target_ip]


        # 4. Excute the command silently
        result = subprocess.run(ping_cmd, stdout=subprocess.DEVNULL, stderr= subprocess.DEVNULL)

        # 5. Check the result
        if result.returncode == 0:
            print(f"[+] Device FOund online: {target_ip}")
            active_devices += 1
    print (f"\n[+] Scan complete. Found {active_devices} active devices on the network.")

if __name__ == "__main__":
 # REPLACE THIS with the first 3 blocks of your actual Ip address
    network_base = "192.168.1"
    scan_network(network_base)
