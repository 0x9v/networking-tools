import sys
import os
import subprocess


def get_auto_base():
    try:
        raw_data = subprocess.check_output(["ip", "route"]).decode("utf-8")
        lines = raw_data.split('\n')

        for line in lines:
            if "default" in line and "src" in line:
                words = line.split()
                src_index = words.index("src")
                active_ip = words[src_index + 1]

                octets = active_ip.split(".")
                return f"{octets[0]}.{octets[1]}.{octets[2]}."

    except Exception:
        return None

    return None


print("========================================")
print("      0x9v icmp network sweeper        ")
print("========================================")
print("type your network base. e.g.: 192.168.0.")

auto_base = get_auto_base()
if auto_base:
    print(f"\n[+] auto-detected network base: {auto_base}")
    network_base = input(f"[>] press ENTER to use default, or type a custom base: ")
    if network_base == "":
        network_base = auto_base
else:
    network_base = input("\n[>] enter network base manually: ")
    if network_base == "":
        print("[-] error: input cannot be empty.")
        sys.exit()

if not network_base.endswith("."):
    print("[-] error: network base must end with a dot (.).")
    print("    example: 192.168.1.")
    sys.exit()

print(f"\n[+] target locked: {network_base}1 to {network_base}254")
print("[*] initiating sweep...\n")

for i in range(1, 255):
    target_ip = f"{network_base}{i}"

    sys.stdout.write(f"\r[*] scanning: {target_ip} ...       ")
    sys.stdout.flush()

    command = f"ping -c 1 -W 1 {target_ip} > /dev/null 2>&1"
    response = os.system(command)

    if response == 0:
        print(f"[+] live host found: {target_ip}")

print("\n[*] sweep complete.")


