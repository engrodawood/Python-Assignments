# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:26:03 2016

@author: Muhammad

module contain support for encryption and decription of text bases on ceasar cipher
algorith

"""
import string
def cleanup(file_name):
    
    """
    Take file as argument and remove spaces and punctuation from the file text
    return originalText and CleanText(text after removing spaces and punctuation)
    
    Arguments : filename
    
    return actualText,cleanText  
    """
    f=open(file_name,'r')
    actualText=f.read()
    cleanText=actualText
    for c in string.punctuation+string.whitespace+string.digits:
        cleanText=cleanText.replace(c,'')
        cleanText=cleanText.lower()
    return actualText,cleanText


def encrypt(cleanText,shift):
    
    """
    Take cleanText(text without spaces and punctuation) and shift a numeric value
    in range 1-26 for encryting text
    
    Arguments : cleanText,shift
    
    return encryptedText  
    """
    
    if shift >=1 and shift <=26:
        encText=""
        for i in cleanText:
            asci_val=ord(i)+shift
            if asci_val>122:
                asci_val-=26
            encText+=chr(asci_val)
        return encText
    else:
        raise SystemExit("Invalid Shift Sorry (shift range is from 1 to 26)")

def decrypt(encText,shift):
    
    """
    Take encryptedText and shift a numeric value
    in range 1-26 as a decryption key
    
    Arguments : encryptedText,shift
    
    return decreptedText  
    """
    decText=""
    for i in encText:
        asci_val=ord(i)-shift
        if asci_val<97:
            asci_val+=26
        decText+=chr(asci_val)
    return decText
    
def freqChar(stringval):
    """
    Take character string and arguement and find most frequest character
    
    Arguments : character String
    
    return character  
    """
    character=''
    max_count=0
    for i in stringval:   
        char_count=stringval.count(i)
        if(char_count>max_count):
            character=i
            max_count=char_count
    return character
    
def breakCipher(encText):
    """
    find the shift based on frequency analysis techniques
    
    Arguments : encrypted Text
    
    return shiftvalue  
    """
    freq_char=freqChar(encText)
    shift=ord(freq_char)-ord('e')
    return shift


