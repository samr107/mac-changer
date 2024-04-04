import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-k", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# Bring wlan0 down
subprocess.run(["ifconfig", interface, "down"])

subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

# Bring wlan0 up
subprocess.run(["ifconfig", interface, "up"])

print("work completed successfully")