# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:46:39 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:00:14 2017

@author: Administrator
"""


import jieba as jb
jb.set_dictionary(r'C:\Users\Administrator\Desktop\test_data\dict.txt')
text=open(r'C:\Users\Administrator\Desktop\test_data\4万病例.txt','r',encoding='utf-8').read()
jb.load_userdict(r'C:\Users\Administrator\Desktop\test_data\cibiao.txt')
outcome=jb.lcut(text,HMM=False)
f = open(r"C:\Users\Administrator\Desktop\test_data\4万病例分词结果.txt", "w+")
for i in range(1, len(outcome)):
    f.write(outcome[i] + "\\" )
f.close()
print(jb.lcut('舌质偏暗',HMM=False))


