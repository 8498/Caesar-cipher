
'''
Created on 27.12.2016

@author: przem
'''

import sys
from Cipher.CeaserCipher import CeaserCipher

def main():
    
    while True:
        print("Witaj w programie do kodowania/dekodowania tekstu za pomocą Szyfru Cezara")
        
        print("Podaj przesunięcie")
        shift = sys.stdin.readline()
        
        print("Chcesz szyfrować czy deszyfrować? (encode/decode)")
        choose = sys.stdin.readline().rstrip('\n')
        
        print("Podaj kod/tekst.")
        chars = sys.stdin.readline()
        
        cipher = CeaserCipher(int(shift))
     
        print(cipher.action(chars, choose) + "\n")
        
if __name__ == "__main__":
    main()