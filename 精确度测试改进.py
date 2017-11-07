# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:04:00 2017

@author: Administrator
"""

import jieba as jb
jb.set_dictionary(r'C:\Users\Administrator\Desktop\test_data\dict.txt')
jb.load_userdict(r'C:\Users\Administrator\Desktop\test_data\cibiao.txt')
text=open(r'C:\Users\Administrator\Desktop\test_data\tt.txt','r',encoding='utf-8').read()

outcome=jb.lcut(text,HMM=False)
f = open(r"C:\Users\Administrator\Desktop\test_data\ceshi.txt", "w+",encoding='utf-8')
for i in range(1, len(outcome)):
    f.write(outcome[i] + "\\" )
f.close()

def cut(string):
    start=0
    out=[]
    for i in range(len(string)):
        if string[i]=='，'or string[i]=='、'or string[i]=='\\'or string[i]=='。'or string[i]=='\n'or string[i]==''or string[i]==',':
            end=i
            new=''
            for j in range(start,end):
                new+=str(string[j])
            if new!='':
                out.append(new)
            start=i+1
    return out

def txt2list(filepath):
    cache=[]
    fd = open(filepath,"r",encoding='utf-8').read()
    cache=cut(fd)
    return cache

def accuracy(filepath1,filepath2):
    num=0
    test=txt2list(filepath2)
    right=txt2list(filepath1)
    for i in range(0,len(test)):
        for j in range(0,len(right)):
            if test[i]==right[j]:
                num=num+1
                right[j]='已经测试过了'
                break
    return num/len(right)

print(accuracy(r'C:\Users\Administrator\Desktop\test_data\yangben.txt',r'C:\Users\Administrator\Desktop\test_data\ceshi.txt'))

