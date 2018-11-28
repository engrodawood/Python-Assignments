# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:45:43 2017

@author: Muhammad
"""
import re

def countWord(inputText):
    """
     Will find the most frequent words in a string and will show list
     of 10 words having most frequency
    """
    
    cleanText=re.sub(r'[\'\!\"\]\[\#\$\%\&\\\'\(\)\*\+\'\,\-\.\/\:\;\<\=\>\?\@\^\_\`\{\|\}\~\'\«\»]','',inputText)
    cleanText=re.sub(r'\d+','',cleanText)
    cleanText=re.sub(' +',' ',cleanText)
    cleanText.strip()
    wordList=list
    wordDict=dict()
    wordDictSorted=dict()
    wordList=cleanText.split(' ')
    for i in wordList:
        wordDict.update({i:wordList.count(i)})
    wordDictSorted=sorted(wordDict.items(), key=lambda x: (-x[1], x[0]))
    wordList=wordDictSorted
    for ch in range(10):
        print("Word : ",wordList[ch][0],"   Frequency: ",wordList[ch][1])
    return

def countChar(inputText):
    """
    Will count most frequent character in any language text
    wil show list of 10 character having msot frequencies
    """
    charDict=dict()
    charList=list
    cleanText=re.sub(r'[\d+\W+]','',inputText)
    for i in cleanText:
        charDict.update({i:cleanText.count(i)})
    charDict=sorted(charDict.items(),key=lambda x:(-x[1],x[0]))
    charList=charDict
    for ch in range(10):
        print("Character : ",charList[ch][0],"   Frequency: ",charList[ch][1])
    return
    
    
    
            
            

    
    
    