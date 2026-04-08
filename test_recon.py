import subprocess

print("[*] initializing automated recon...")
print("[*] fetching local routine table...\n")

raw_data = subprocess.check_output(["ip", "route"]).decode("utf-8")

lines = raw_data.split('\n')

active_ip = ""

for line in lines:
    if "default" in line and "src" in line:
        words = line.split()
        src_index = words.index("src")
        active_ip = words[src_index + 1]
        break

print(f"[+] extracted active ip: {active_ip}")

octets = active_ip.split('.')

network_base = f"{octets[0]}.{octets[1]}.{octets[2]}."

print(f"[+] computer network base: {network_base}")
