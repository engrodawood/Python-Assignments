# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:45:43 2017

@author: Muhammad
"""

import string

def countWord(inputText):
    import re
    cleanText=re.sub(r'[\'\!\"\]\[\#\$\%\&\\\'\(\)\*\+\'\,\-\.\/\:\;\<\=\>\?\@\^\_\`\{\|\}\~\'\«\»]','',inputText)
    cleanText=re.sub(r'\d+','',cleanText)
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
        print(wordList[ch])
    return

def countChar(inputText):
    import re
    charDict=dict()
    charList=list
    cleanText=re.sub(r'[\d+\W+]','',inputText)
    for i in cleanText:
        charDict.update({i:cleanText.count(i)})
    charDict=sorted(charDict.items(),key=lambda x:(-x[1],x[0]))
    charList=charDict
    for ch in range(10):
        print(charList[ch])
    return
    
def cleanup(actualText):
    
    """
    Take file as argument and remove spaces and punctuation from the file text
    return originalText and CleanText(text after removing spaces and punctuation)
    
    Arguments : filename
    
    return actualText,cleanText  
    """
    cleanText=actualText
    for c in string.punctuation+string.digits:
        cleanText=cleanText.replace(c,'')
        cleanText=cleanText.lower()
    return actualText,cleanText   
    
countChar("حمد یوسف (سابقہ نام یوسف یوحنا؛ پیدائش: 27 اگست 1974ء) سابق پاکستانی کرکٹر ہیں۔ 2005ء میں قبول اسلام سے قبل، یوسف کا شمار پاکستان کرکٹ ٹیم کی طرف سے کھیلنے والے چند مسیحی کھلاڑیوں میں ہوتا تھا۔ غریب پس منظر سے تعلق رکھنے والے یوسف نے عمدہ بلے بازی کے باعث اپنی پہچان بنائی اور کرکٹ کی تاریخ میں کئی ریکارڈ اپنے نام کیے۔ یوسف نے اپنے ٹیسٹ کیریئر میں ساڑھے سات ہزار رنز، اور ایک روزہ کیریئر میں ساڑھے نو ہزار رنز بنائ")
print("Printing word now\n\n")
countWord("حمد یوسف (سابقہ نام یوسف یوحنا؛ پیدائش: 27 اگست 1974ء) سابق پاکستانی کرکٹر ہیں۔ 2005ء میں قبول اسلام سے قبل، یوسف کا شمار پاکستان کرکٹ ٹیم کی طرف سے کھیلنے والے چند مسیحی کھلاڑیوں میں ہوتا تھا۔ غریب پس منظر سے تعلق رکھنے والے یوسف نے عمدہ بلے بازی کے باعث اپنی پہچان بنائی اور کرکٹ کی تاریخ میں کئی ریکارڈ اپنے نام کیے۔ یوسف نے اپنے ٹیسٹ کیریئر میں ساڑھے سات ہزار رنز، اور ایک روزہ کیریئر میں ساڑھے نو ہزار رنز بنائ")

print();
countChar("إن ويكي مصدر لا تضمن صحة ودقة المعلومات. إن هذا المشروع هو مشروع على شبكة الإنترنت لاحتواء نصوص حرة والتي يقوم مجموعة من المتطوعين بتجميعها وتنسيقها. لذا فإن المواد المتوافرة قد لا تكون قد تمت مراجعتها من قبل أخصائيين معترف لهم بالاختصاص في مجال معين لتأكيد دقتها وصحتها. بالإضافة إلى ذلك فإن النصوص محفوظة كما هي وأي أخطاء قد قام بها المؤلف تنشر كما هي للمحافظة على أمانة العمل.")
print()
countWord("إن ويكي مصدر لا تضمن صحة ودقة المعلومات. إن هذا المشروع هو مشروع على شبكة الإنترنت لاحتواء نصوص حرة والتي يقوم مجموعة من المتطوعين بتجميعها وتنسيقها. لذا فإن المواد المتوافرة قد لا تكون قد تمت مراجعتها من قبل أخصائيين معترف لهم بالاختصاص في مجال معين لتأكيد دقتها وصحتها. بالإضافة إلى ذلك فإن النصوص محفوظة كما هي وأي أخطاء قد قام بها المؤلف تنشر كما هي للمحافظة على أمانة العمل.")

#cleanText=re.sub(r'[\'\!\"\#\$\%\&\\\'\(\)\*\+\'\,\-\.\/\:\;\<\=\>\?\@\^\_\`\{\|\}\~\']','',inputText)
