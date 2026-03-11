import subprocess
import datetime

def run_audit():
    print("[*] Starting System Security Audit...")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Check for Open Ports (using 'ss' - Socket Statistics)
    print("[*] Checking open ports...")
    # 'ss -tuln' looks for Listening TCP/UDP ports numerically
    ports = subprocess.check_output(["ss", "-tuln"]).decode("utf-8")
    
    # 2. Check for Top 5 Memory-Consuming Processes
    print("[*] Auditing running processes...")
    # FIXED: changed --sort=-%memm to --sort=-%mem
    processes = subprocess.check_output(["ps", "-aux", "--sort=-%mem"]).decode("utf-8").splitlines()[:6]
    processes_output = "\n".join(processes)

    # 3. Write results to a Report File
    with open("audit_results.txt", "a") as f:
        f.write(f"SYSTEM SECURITY REPORT - {timestamp}\n")
        f.write("="*40 + "\n\n")
        f.write("OPEN PORTS (TCP/UDP):\n")
        f.write(ports + "\n")
        f.write("="*40 + "\n")
        f.write("TOP 5 PROCESSES (BY MEMORY):\n")
        f.write(processes_output + "\n")
    
    print(f"[+] Audit complete. Results saved to 'audit_results.txt'.")

if __name__ == "__main__":
    run_audit()
