# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:43:52 2018

@author: nic
"""

import numpy as np
import pandas as pd



import random 
import nltk

from nltk.corpus import wordnet
#nltk.download('wordnet')

words = []

for j in range(100):
    
    letters = ['c','u','i','o','s']
    word = []
    
    for i in range(3):
        extract = random.randint(0,len(letters)-1)
        letr = letters[extract]
        letters.pop(extract)
        word.append(letr)
    
    words.append(''.join(str(e) for e in word) + 'n')

real_words = []



words = set(words)

for j in words:
    if not wordnet.synsets(j):
        pass
    else:
        real_words.append(j)
      
      