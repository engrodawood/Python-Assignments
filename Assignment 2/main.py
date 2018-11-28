# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 10:26:59 2017

@author: Muhammad
"""
from caesar import cleanup,encrypt,decrypt,breakCipher
import random

file_name=input("Enter File name You want to encrypt along with file Extension ! ")
actualText,cleanText=cleanup(file_name)

print("\nActual Text:\n ",actualText)
print("\n\nClean Text: \n",cleanText)
shift=random.randint(1,26)
encText=encrypt(cleanText,shift)
print("\n\nEncrypted Text: \n",encText)
predShift=breakCipher(encText)
print("\n\nPredicted Shift is : ",predShift," and Actual Shift is : ",shift)
decText=decrypt(encText,predShift)
print("\n\nResult of Breaking Cipher is : \n",decText)