'''
Created on 27.12.2016

@author: przem
'''

from collections import Counter

class CeaserCipher(object):
    '''
    classdocs
    '''
    param = ""
    shift = 0
    code = ""

    def __init__(self, shift):
        
        self.shift = shift
        self.code = ""
        self.text = ""
    
    def action(self, chars, choose):
        
        if(choose == 'encode'):
            return self.encode(chars)
            
        elif(choose == 'decode'):
            return self.decode(chars)
            
        else:
            return "Nie wybrałeś co zrobić"
    
    
    def encode(self, text):
        
        text = text.upper()
        
        for text_char in text:   
            
            text_char = ord(text_char)
            
            if self.checkLetter(text_char):
                charx = divmod(text_char - 65 + self.shift, 26)
                text_char =  charx[1] + 65 
            
            self.code = self.code + chr(text_char)
                
        return self.code
    
    def decode(self, code = ""):
        
        if(code):
            
            for code_char in code:
                
                code_char = ord(code_char)
                
                if self.checkLetter(code_char):
                    charx = divmod(code_char - 65 - self.shift, 26)
                    code_char = charx[1] + 65 
                    
                self.text = self.text + chr(code_char)
            
            return self.text

        elif(self.code):
            print(self.code)
            
            for code_char in self.code:
                
                code_char = ord(code_char)
                
                if self.checkLetter(code_char):
                    charx = divmod(code_char - 65 - self.shift, 26)
                    code_char = charx[1] + 65 
                    
                self.text = self.text + chr(code_char)
            
            return self.text
        
        else:
            return "Coś poszło nie tak"
    
    def checkLetter(self, char):
        
        if 65 < char < 90:
            return True
        
        
        