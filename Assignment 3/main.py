# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:20:20 2017

@author: Muhammad
"""


import wikipedia as wiki
from frequency import countWord,countChar

wiki.set_lang("ps") #Setting the language to Urdu
#All language codes available at: http://meta.wikimedia.org/wiki/List_of_Wikipedias

def getWikiPage(s):
    """
    This function returns the page associated with a given Wikipedia title string. 
    If there are multiple pages associated with a title string, it picks the
    first one in the disambiguation of that page.
    Input: s (Wikipedia page title)
    Return: Wikipedia Python API page object
    """
    try:
        p = wiki.page(s)
    except wiki.exceptions.DisambiguationError as disambiguation:
        #This exception is raised if there are multiple Wikipedia pages associated with the given title
        print (disambiguation) #We display the titles of all the pages
        print ("Warning: Picking",disambiguation.options[0]) #But we pick the first one
        s = disambiguation.options[0] #Like this!
        p = wiki.page(s)
    return p

  #Use wiki.random() to Pick a random title from Wikipedia.

for i in range(10):
    s=wiki.random()
    print ("The string for wikipedia is:",s) 
    
    try:
        p=getWikiPage(s)
    except Exception as e: 
        #Just in case there are any unexpected errors
        print ('Failed to access the page associated with \'',wiki.random(),'\'. The error returned is: ',e)
    else: #If everything goes well, print stuff!
       # print ('*'*10,"Title",p.title,'*'*10+'\n')
        #print ('*'*10,"id",p.pageid,'*'*10+'\n')
        #print ('*'*10,"Summary",'*'*10+'\n',p.summary)    
        print ('*'*10,"Content",'*'*10+'\n',p.content)
        #print ('*'*10,"Links",'*'*10+'\n','\n'.join(p.links)) #just for fun!
        #counting frequent character in article
        print('\n\n'+'*'*10," Finding Frequent Character ",'*'*10+'\n')
        countChar(p.content)
        print('\n\n'+'*'*10," Finding Frequent Word ",'*'*10+'\n')
        countWord(p.content)
