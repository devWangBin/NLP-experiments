# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:31:10 2019
实验3 NLP
@author:wangbin
"""

import time
import jieba
import jieba.posseg as pseg  
from snownlp import SnowNLP
import thulac	
import pynlpir
from stanfordcorenlp import StanfordCoreNLP
import nltk
import spacy 
from nltk.corpus import treebank
from pyhanlp import *



spacy_nlp = spacy.load('en_core_web_sm')

def chinese_Txt_test(document):
    """
    hanlp中文测试
    """
    print(">>>>>hanlp tagging start...")
    start = time.process_time()
    
    result0 = HanLP.segment(document)
    
    elapsed = (time.process_time() - start)  
    print("hanlp Time used:",elapsed)
    print("《《hanlp》》: " )  
    
    for term in result0:
        print('{}--{}\t'.format(term.word, term.nature),end=' ') # 获取单词与词性
    print("\n")
    
    """
    测试工具包jieba词性标注
    """
    print(">>>>>jieba tagging start...")
    start = time.process_time()
    
    result1 = pseg.lcut(document)
    
    elapsed = (time.process_time() - start)  
    print("jieba Time used:",elapsed)
    print("《《jieba》》: " )  
    for word,tag in result1:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    
    """
    测试工具包SnowNLP
    """
    print(">>>>>SnowNLP tagging start...")
    start = time.process_time()
    s = SnowNLP(document)
    result2 = s.tags                
    elapsed = (time.process_time() - start)
    print("SnowNLP Time used:",elapsed)
    print("《《SnowNLP》》: " )  
    for word,tag in result2:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    
    """
    测试StanfordCoreNLP工具包
    """
    print(">>>>>StanfordCoreNLP tagging start...")
    start = time.process_time()
    nlp = StanfordCoreNLP(r'C:\Users\93568\Desktop\NLP实验\stanford-corenlp-full-2018-02-27',lang = 'zh')
    result3 = nlp.pos_tag(document)
    elapsed = (time.process_time() - start)
    print("StanfordCoreNLP Time used:",elapsed)
    print("《《StanfordCoreNLP》》: " )
    for word,tag in result3:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    #StanfordCoreNLP 'Named Entities:', nlp.ner(sentence)
    print(">>>>>StanfordCoreNLP Named Entities start...")
    start = time.process_time()
    result4 = nlp.ner(document)
    elapsed = (time.process_time() - start)
    print("StanfordCoreNLP Named Entities Time used:",elapsed)
    print("《《StanfordCoreNLP》》: " )
    nlp.close() 
    for word,tag in result4:
        if tag != 'O':
            print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    
    """
    测试thulac工具包
    """
    print(">>>>>thulac tagging start...")
    start = time.process_time()
    
    thu1 = thulac.thulac()  #默认模式
    text2d = thu1.cut(document, text=False)  #进行一句话分词
    
    elapsed = (time.process_time() - start)
    print("thulac Time used:",elapsed)
    print("《《thulac》》: ")
    for tu in text2d:
        print(str(tu[0])+"--"+str(tu[1])+"\t", end=' ')
    print('\n')
    
    
    """
    测试pynlpir工具包
    """
    print(">>>>>pynlpir tagging start...")
    start = time.process_time()
    pynlpir.open()
    result5 = pynlpir.segment(document)
    elapsed = (time.process_time() - start)
    print("pynlpir Time used:",elapsed)
    print("《《pynlpir》》:") 
    for word,tag in result5:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")

def english_Txt_test(doc):
    print(">>>>>NLTK tokenization start...")
    start = time.process_time()
    
    tokens = nltk.word_tokenize(doc)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    t = treebank.parsed_sents('wsj_0001.mrg')[0]
    t.draw()  
    elapsed = (time.process_time() - start)    
    print("NLTK Time used:",elapsed)
    print("《《NLTK》》: " )
    for word,tag in tagged:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    """
    英文分词spacy
    """
    print(">>>>>spacy tagging start...")
    start = time.process_time()
    s_doc = spacy_nlp(doc)
    
    elapsed = (time.process_time() - start)
    print("spacy Time used:",elapsed)
    print("《《Spacy》》: ")
    for token in s_doc:
        print(str(token)+ "--"+str(token.pos_)+"\t", end=' ')
    print("\n")
    for ent in s_doc.ents:
        print(ent,"----", ent.label_, ent.label)
    print("\n")
    """
    英文分词StanfordCoreNLP
    """
    print(">>>>>StanfordCoreNLP tagging start...")
    start = time.process_time()
    nlp2 = StanfordCoreNLP(r'C:\Users\93568\Desktop\NLP实验\stanford-corenlp-full-2018-02-27')
     
    result7 =  nlp2.pos_tag(doc)

    elapsed = (time.process_time() - start)
    print("StanfordCoreNLP Time used:",elapsed)
    print("《《StanfordCoreNLP>>: " )
   
    for word,tag in result7:   
        print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    
    #StanfordCoreNLP 'Named Entities:', nlp.ner(sentence)
    print(">>>>>StanfordCoreNLP Named Entities start...")
    start = time.process_time()
    
    result8 =  nlp2.ner(doc)

    elapsed = (time.process_time() - start)
    print("StanfordCoreNLP Named Entities Time used:",elapsed)
    print("《《StanfordCoreNLP》》: " )
    nlp2.close() 
    for word,tag in result8:
        if tag != 'O':
            print(str(word)+"--"+str(tag)+"\t", end=' ')
    print("\n")
    


def main():
    
    f = open('Chinese.txt')
    document = f.read()
    f.close()
    print(document)    
    chinese_Txt_test(document)
    
    f = open('English.txt')
    doc = f.read()
    f.close()
    print(doc)
    print("\n")  
    english_Txt_test(doc)
    
    print("test finished!")
    
    
    
        
if __name__ == '__main__':
    main() 
