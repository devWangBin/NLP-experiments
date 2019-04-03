# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:36:20 2019
@author: wangbin
"""
import os
from stanfordcorenlp import StanfordCoreNLP
from pyltp import Parser
from pyltp import Segmentor
from pyltp import Postagger

    
def test_Snlp_en(document):
    
    print("start stanfordcorenlp parse and dependency_parse with English:>>>")    
    nlp = StanfordCoreNLP(r'D:\anaconda\Lib\stanford-corenlp-full-2018-02-27')
    pra = nlp.parse(document)

    d_pra = nlp.dependency_parse(document)
        
    nlp.close() # Do not forget to close! The backend server will consume a lot memery.
        
    print("parse: \n",pra)
    print("dependency_parse: \n",d_pra)

def test_Snlp_zh(document):
    
    print("start stanfordcorenlp parse and dependency_parse with Chinese:>>>")       
    nlp = StanfordCoreNLP(r'D:\anaconda\Lib\stanford-corenlp-full-2018-02-27',lang = 'zh')
    pra = nlp.parse(document)

    d_pra = nlp.dependency_parse(document)
        
    nlp.close() # Do not forget to close! The backend server will consume a lot memery.
        
    print("parse: \n",pra)
    print("dependency_parse: \n",d_pra)
        

def test_ltp(document):
    
    LTP_DATA_DIR = r"D:\anaconda\envs\TF+3.5\Lib\site-packages\pyltp-model"
    # ltp模型目录的路径
    par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    words = segmentor.segment(document)  # 分词
    print("\nA")
    print("分词结果：")
    print ('\t'.join(words))
    segmentor.release()  # 释放模型
    
    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    print("\n")
    print("词性标注结果：")
    print ('\t'.join(postags))
    postagger.release()  # 释放模型
    
    parser = Parser() # 初始化实例
    parser.load(par_model_path)  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print("\n")
    print("句法分析结果：")
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()  # 释放模型
    

def main():
    
    f = open('chinese_sen2.txt','r',encoding='utf-8',errors='ignore')
    document = f.read()
    f.close()
    print(document) 
    print("start ltp chinese test>>>")
    test_ltp(document)
    test_Snlp_zh(document)
        
    f = open('english_sen.txt')
    doc = f.read()
    f.close()
    print(doc)
    print("\n")  
    test_Snlp_zh(doc)
    
    print("test finished!")
            
if __name__ == '__main__':
    main() 