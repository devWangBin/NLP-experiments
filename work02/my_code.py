# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 09:43:47 2019
@author: wangbin
"""
import time
import jieba
from snownlp import SnowNLP
import thulac	
import pynlpir
from stanfordcorenlp import StanfordCoreNLP
import nltk
import spacy 
spacy_nlp = spacy.load('en_core_web_sm')

f = open('Chinese.txt')
document = f.read()
f.close()
print(document)    

"""
测试工具包jieba
"""
print(">>>>>jieba tokenization start...")
start = time.process_time()

seg_list = jieba.cut(str(document), cut_all=True)

elapsed = (time.process_time() - start)
print("jieba 01 Time used:",elapsed)

print("《《jieba Full Mode》》: \n" + "/ ".join(seg_list))  # 全模式

start = time.process_time()
seg_list = jieba.cut(document, cut_all=False)
elapsed = (time.process_time() - start)
print("jieba 02 Time used:",elapsed)
print("《《jieba Default Mode》》: \n" + "/ ".join(seg_list))  # 精确模式

start = time.process_time()
seg_list = jieba.cut_for_search(document)  # 搜索引擎模式
elapsed = (time.process_time() - start)
print("jieba 03 Time used:",elapsed)
print("《《jieba Search Model》》: \n" + "/ ".join(seg_list))

"""
测试工具包SnowNLP
"""
print(">>>>>SnowNLP tokenization start...")
start = time.process_time()
s = SnowNLP(document)
result = s.words                    # [u'这个', u'东西', u'真心',
elapsed = (time.process_time() - start)
print("SnowNLP Time used:",elapsed)
print("《《SnowNLP》》: \n" + "/ ".join(result))                        #  u'很', u'赞']
#result = s.tags          # [(u'这个', u'r'), (u'东西', u'n'),
#print(result)                #  (u'真心', u'd'), (u'很', u'd'),
#                        #  (u'赞', u'Vg')]
#result = s.sentiments    # 0.9769663402895832 positive的概率
#print(result)
#result = s.pinyin        # [u'zhe', u'ge', u'dong', u'xi',
#print(result)                #  u'zhen', u'xin', u'hen', u'zan']
#s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
#
#s.han           # u'「繁体字」「繁体中文」的叫法
#                # 在台湾亦很常见。'
"""
测试thulac工具包
"""
print(">>>>>thulac tokenization start...")
start = time.process_time()
thu1 = thulac.thulac(seg_only=True)  #默认模式
text = thu1.cut(document, text=True)  #进行一句话分词
elapsed = (time.process_time() - start)
print("thulac Time used:",elapsed)
print("《《thulac》》: \n" + "/ ".join(text))    
#thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
#thu1.cut_f("Chinese.txt", "output.txt")  #对input.txt文件内容进行分词，输出到output.txt

"""
测试pynlpir工具包
"""
print(">>>>>pynlpir tokenization start...")
start = time.process_time()
pynlpir.open()
resu = pynlpir.segment(document,pos_tagging=False)

elapsed = (time.process_time() - start)
print("pynlpir Time used:",elapsed)

print("《《pynlpir》》: \n" + "/ ".join(resu)) 
"""
pynlpir.segment(s, pos_tagging=True, pos_names=‘parent‘, pos_english=True)
pynlpir.get_key_words(s, max_words=50, weighted=False)
分詞：pynlpir.segment(s, pos_tagging=True, pos_names=‘parent‘, pos_english=True) 
S: 句子 
pos_tagging：是否進行詞性標註 
pos_names：顯示詞性的父類(parent)還是子類(child) 或者全部(all) 
pos_english：詞性顯示英語還是中文
获取关键词：pynlpir.get_key_words(s, max_words=50, weighted=False) 
s: 句子 
max_words：最大的關鍵詞數 
weighted：是否顯示關鍵詞的權重
"""
"""
测试StanfordCoreNLP工具包
"""
print(">>>>>StanfordCoreNLP tokenization start...")
start = time.process_time()
nlp = StanfordCoreNLP(r'C:\Users\93568\Desktop\NLP实验\stanford-corenlp-full-2018-02-27',lang = 'zh')
outWords = nlp.word_tokenize(document)
elapsed = (time.process_time() - start)
print("StanfordCoreNLP Time used:",elapsed)
print("《《StanfordCoreNLP》》: \n" + "/ ".join(outWords))
#print 'Part of Speech:', nlp.pos_tag(sentence)
#print 'Named Entities:', nlp.ner(sentence)
#print 'Constituency Parsing:', nlp.parse(sentence)
#print 'Dependency Parsing:', nlp.dependency_parse(sentence)
nlp.close() # Do not forget to close! The backend server will consume a lot memery.

"""
英文分词NLTK
"""
f = open('English.txt')
doc = f.read()
f.close()
print(doc)

print(">>>>>NLTK tokenization start...")
start = time.process_time()
tokens = nltk.word_tokenize(doc)
elapsed = (time.process_time() - start)
print("NLTK Time used:",elapsed)
print("《《NLTK》》: \n" + "/ ".join(tokens))

"""
英文分词spacy
"""
print(">>>>>spacy tokenization start...")
start = time.process_time()
s_doc = spacy_nlp(doc)
elapsed = (time.process_time() - start)
print("spacy Time used:",elapsed)

token_doc =[]
for token in s_doc:
    token = str(token)
    token_doc.append(token)
print("《《Spacy》》: \n" + "/ ".join(token_doc))

"""
英文分词StanfordCoreNLP
"""
print(">>>>>StanfordCoreNLP tokenization start...")
start = time.process_time()
nlp2 = StanfordCoreNLP(r'C:\Users\93568\Desktop\NLP实验\stanford-corenlp-full-2018-02-27')
outWords = nlp2.word_tokenize(doc)
elapsed = (time.process_time() - start)
print("StanfordCoreNLP Time used:",elapsed)
print("《《StanfordCoreNLP>>: \n" + "/ ".join(outWords))
nlp2.close() # Do not forget to close! The backend server will consume a lot memery.