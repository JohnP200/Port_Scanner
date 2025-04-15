# Port Scanner (Python)

This is a simple TCP port scanner written in Python. It checks a list of common ports on a target IP address or hostname to see which ones are open.

## How It Works

- Uses Python's 'socket' module to connect to each port.
- Reports any ports that open.

## Usage 

Run it from the terminal

```bash
python port_scanner.py

## Example
Enter the host to scan (e.g., 127.0.0.1): 127.0.0.1
[*] Scanning 127.0.0.1...

[+] Port 22 is open
[+] Port 80 is open

## Disclaimer
This tool is for eductional purposes only. Unathorized port scanning is illegal and unethical.