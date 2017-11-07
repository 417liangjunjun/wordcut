# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:38:06 2017

@author: Administrator
"""

import jieba as jb
jb.set_dictionary(r'C:\Users\Administrator\Desktop\test_data\dict.txt')
text=open(r'C:\Users\Administrator\Desktop\test_data\4万病例.txt','r',encoding='utf-8').read()
jb.load_userdict(r'C:\Users\Administrator\Desktop\test_data\cibiao.txt')
words=jb.lcut(text,HMM=False)
word_freq = {}  
for word in words:  
    if word in word_freq:  
        word_freq[word] += 1  
    else:  
        word_freq[word] = 1  
  
freq_word = []  
for word, freq in word_freq.items():  
    freq_word.append((word, freq))  
freq_word.sort(key = lambda x: x[1], reverse = True) 
f = open(r"C:\Users\Administrator\Desktop\test_data\4万病例分词结果.txt", "w+",encoding='utf-8')
for i in range(1, len(freq_word)):
    if len(list(freq_word[i])[0])>1 and len(list(freq_word[i])[0])<5:
        f.write(list(freq_word[i])[0]+' '+str(list(freq_word[i])[1])+'\n')
f.close()
