import sys
import os

print("========================================")
print("      0x9v icmp network sweeper        ")
print("========================================")
print("type your network base. e.g.: 192.168.0.")

network_base = input("\n[>] enter network base: ")

if network_base == "":
    print("[x] error: input cannot be empty.")
    sys.exit()

elif not network_base.endswith("."):
    print("[x] error: your network base must end with a dot (.).")
    print("    example: 192.168.1.")
    sys.exit()

else:
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


