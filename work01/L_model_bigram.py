# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:52:22 2019

@author: 93568
"""
from textblob import TextBlob
from textblob import Word
from collections import defaultdict
import re
import math

postings = defaultdict(dict)    #存放词频信息的postings

pre_postings = defaultdict(dict)

V = 0 							#语料词汇量

def main():
    global postings,pre_postings,V
    get_dic()
    V = len(pre_postings)-1
    print("V:"+str(V))
#    print(pre_postings)
#    print(postings)
    cal_probability()
#    print(postings) 
    print("get here~~~")
    ppl = test()   
    print("the test PPL score is:"+str(round(ppl,5)))


def get_dic():
    
    global postings,pre_postings
    f = open('train_LM.txt','r',encoding='utf-8',errors='ignore')
    document = f.read()
    f.close()
    
    document=document.lower()
    document=re.sub(r"\W|\d|\s{2,}"," ",document)#保留字母下划线
    document=re.sub(r"\s{2,}"," ",document)
    document = document.replace('__eou__','\t') #将__eou__替换为分割符号
    sentences = document.split('\t')
    
    if sentences[-1]=="":
        sentences.pop()
        print("pop one ...")
#    print(sentences)   
    for sen in sentences:        
        terms=TextBlob(sen).words.singularize()
        
        result=[]
        for word in terms:
            expected_str = Word(word)
            expected_str = expected_str.lemmatize("v")
            result.append(expected_str)
                                 
        result.insert(0,"s**s")
        result.append("e**e")
        
        i = 1
        while i < len(result):
            
            str1 = result[i-1]
            
            strr = str1 + '$' + result[i]
            
            if strr in postings:
                postings[strr][0] += 1
            else:
                postings[strr][0] = 1
            
            if str1 in pre_postings:
                pre_postings[str1] +=1
            else:
                pre_postings[str1] =1
            i+=1
    
#    print(pre_postings)
    
    

def cal_probability():
    global postings,pre_postings,V

    for term in postings:
        inde = term.split('$')[0]
#        print(term)
#        print(inde)
        postings[term][1] = postings[term][0]/pre_postings[inde]
        


def get_pw_of_absent(newTerm):
    #根据在测试集中新出现的词来更新语料库的词概率信息（加 1 法） 
    global pre_postings,V
	
    tem = newTerm.slipt('$')[0]
    pw = 0.0
    
    if tem in pre_postings:
        #第一种将|V|换为了 Wi-1 词后能出现的词的可能数，
        #之前为pre_postings[Wi-1]次里面去重后的种类数——set(...)<<|V| 一般远小于
        #再加一种为现在可能的种数
        #但是这种平滑可能会导致新出现的词元的概率比较大，应当回过头去将其它可能的情况的词元概率也做修改，重新计算
        #本计算为了简化就不做修改，分母加|V|,使新词的概率比较小，一定程度上认为原训练语料库的数据可靠性高
        #新出现的词只是很小概率的事
        #pw = 1/(pre_postings[tem]+set(pre_postings[tem])+1)
        pw = 1/(pre_postings[tem]+V)
    
    else:
        #pw = 1/(0+0+1)
        pw = 1/V
        
    return pw

    


def test():
    global postings
    
    log_PT = 0
    f = open('test_LM.txt','r',encoding='utf-8',errors='ignore')
    document = f.read()
    f.close()

    test_wNum = 0
    
    document=document.lower()
    document=re.sub(r"\W|\d|\s{2,}"," ",document)#保留字母下划线
    document=re.sub(r"\s{2,}"," ",document)
    document = document.replace('__eou__','\t') #将__eou__替换为分割符号
    sentences = document.split('\t')
    
    if sentences[-1]=="":
        sentences.pop()
        print("pop one ...")
    
    for sen in sentences:        
        terms=TextBlob(sen).words.singularize()
        
        result=[]
        for word in terms:
            expected_str = Word(word)
            expected_str = expected_str.lemmatize("v")
            result.append(expected_str)
                      
        result.insert(0,"s**s")
        result.append("e**e")
        
        i = 1
        while i < len(result):
            
            strr = result[i-1] + '$' + result[i]
            test_wNum += 1
            if strr in postings:				
                log_PT += math.log(postings[strr][1],2)
            else:
                print("one not in posting!!!")
                temp = get_pw_of_absent(strr)
                log_PT += math.log(temp,2)
            i+=1

    print("log_PT:"+str(log_PT))
    print("test_num:"+str(test_wNum))
    PPL = pow(2,-log_PT/test_wNum)  
    return PPL  
            
if __name__ == "__main__":
    main()
