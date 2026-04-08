# sweeper.py
> a lightweight python-based cli tool that maps local network with automated subnet detection.
## overview
> 
> the script operates without needing heavy external dependencies like nmap, providing a rapid local host mapping solution.
- **the engine:** silently interrogates the OS to extract the active network interface and calculate the local network base.
- **the experience:** features an interactive cli with a real-time carriage return heartbeat log, strict input validation, and robust error handling.
> the goal is to have a rapid local host mapping without nmap dependencies

## prerequisites
- **python 3.x**, uses only standard built-in libraries (no `pip install` required)
- **environment:** a linux/unix system. the script relies on the native `ip route` utility for auto-detection and specific linux `ping` flags (`-c`, `-W`)

## installation
```bash
gh repo clone 0x9v/networking-tools
cd networking-tools
```

## usage
> execute the script from the terminal:
```bash
python sweeper.py
```
the script will automatically detect your network base. you can simply press `Enter` to accept the default target, or manually override it providing a custom base (e.g., `192.168.0`)
