import requests
from termcolor import colored
import argparse
import time


parser = argparse.ArgumentParser(description='Modo de uso: ''-u https://google.com -w wordlist.txt')
parser.add_argument('-u', '--url', required=True, type=str, help='')
parser.add_argument('-w', '--wordlist', required=True, type=str, help='')


args = parser.parse_args()
url = args.url
wordlist_path = args.wordlist


response = requests.get(url)
headers = response.headers

size = 0
try:

    with open(wordlist_path, "r") as f:
        lista = f.readlines()

    for linha in lista:
        payload = linha.strip()
        for chunk in response.iter_content(1024):
            size += len(chunk)
        for key in headers.keys():
            headers[key] = payload
            start = time.perf_counter()
            response = requests.get(url, headers=headers)
            end = time.perf_counter()
            tempo_total = end - start  
            response_time = round(tempo_total, 2)         
            print (colored(f'{key}: {headers[key]}', 'green'))
            print (colored(f'StatusCode= {response.status_code}', 'green') )
            print (colored(f'Tamanho da resposta= {size}', 'green'))
            print (colored(f'Tempo total da resposta= {response_time}', 'green'))
            print (colored('===============================================','red'))

    
    while True:
        pass
except KeyboardInterrupt:
    print(colored("Você interrompeu o programa",'red'))
