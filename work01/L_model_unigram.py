# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:10:22 2019

@author: wangbin
"""
from textblob import TextBlob
from textblob import Word
from collections import defaultdict
from functools import reduce 
import re
import math
from sklearn.externals import joblib


dictionary = set()              #文档词典

postings = defaultdict(dict)    #存放词频信息的postings

total_num = 0                   #总词频数

num_dic = 0                     #总词个数


def main():
    global postings,total_num,num_dic,dictionary
    
    get_dic()
    cal_probability()
    num_dic = len(dictionary)
    
#    joblib.dump(postings, 'uni_gram_postings.pkl')
#    postings = joblib.load('uni_gram_postings.pkl')
    
    print("Total number of train words:"+str(total_num))
    print("number of dictionary:"+str(num_dic))

    ppl = test()
   
    print("the test PPL score is:"+str(round(ppl,5)))


def get_dic():
    global dictionary,total_num,postings
    f = open('train_LM.txt','r',encoding='utf-8',errors='ignore')
    lines = f.readlines()
    f.close()

    for line in lines:
        terms = line_token(line)
        #print(terms)
        d_tnum=len(terms)#预处理后每篇文档的总词数
        #print(d_tnum)
        unique_terms = set(terms)
        dictionary = dictionary.union(unique_terms)#并入总词典
        total_num += d_tnum
        
        for term in unique_terms:
            
            c_term=terms.count(term)
            if term in postings:
                postings[term][0] += c_term
            else:
                postings[term][0] = c_term

       
    
    
def line_token(document):

    document=document.lower()
    document = document.replace('__eou__','') #将__eou__删除  
    #document=re.sub(r'', " ",document)
    #document=re.sub(r"\W|\d|_|\s{2,}"," ",document)#\W只保留数字字母下划线。\d匹配任意数字 \s{2，}匹配两个以上的空格
    document=re.sub(r"\W|\d|\s{2,}"," ",document)#保留数字和下划线
    terms=TextBlob(document).words.singularize()
    result=[]
    for word in terms:
        expected_str = Word(word)
        expected_str = expected_str.lemmatize("v")#还原动词原型
        result.append(expected_str)
    return result     
  

def cal_probability():
    global postings,total_num
    
    for term in postings:
        postings[term][1] = postings[term][0]/total_num
        



def get_pw_of_absent(newTerm):
    #根据在测试集中新出现的词来更新语料库的词概率信息（加 1 法）
    
    global total_num,num_dic
    
    return 1/(total_num + num_dic)
    


def test():
    global postings
    log_PT = 0
    f = open('test_LM.txt','r',encoding='utf-8',errors='ignore')
    document = f.read()
    f.close()
    test_wNum = 0
    words = line_token(document)
    for expected_str in words:
        test_wNum += 1
        #加 1 法平滑
        if expected_str in postings:
            log_PT += math.log(postings[expected_str][1],2)
        else:
#            print("update_posting!!!")
#            update_postings_dic(expected_str)
#            log_PT += math.log(postings[expected_str][1],2)
            print("one not in posting!!!")
            temp = get_pw_of_absent(str)
            log_PT += math.log(temp,2)
    print("log_PT:"+str(log_PT))
    print("test_num:"+str(test_wNum))
    PPL = pow(2,-log_PT/test_wNum)  
    return PPL
"""
#    document=re.sub(r"\W|\d|\s{2,}"," ",document)#保留字母下划线
#    document = document.replace('__eou__','\t') #将__eou__替换为分割符号
#    sentences = document.split('\t')
#    
#    for sen in sentences:
#        terms=TextBlob(sen).words.singularize()
#        
#        for word in terms:
#            expected_str = Word(word)
#            expected_str = expected_str.lemmatize("v")#还原动词原型
#            #加 1 法平滑
#            if expected_str in postings:
#                log_PT += math.log(postings[expected_str][1])
#            else:
#                update_postings_dic(expected_str)
#                log_PT += math.log(postings[expected_str][1])
#        print(sen)
"""  
if __name__ == "__main__":
    main()