
# Description:将中文简体Wiki使用正则表达式处理,暂时作为函数库
# Author：Yang Jiang
# Prompt: code in Python3 env

import re
import jieba
import sys
import os

from const import common_dir


#读取停用词
def stopwordslist():
    stopword_dir = os.path.join(common_dir, "stopwords.txt")
    stopwords = [line.strip() for line in open(stopword_dir, encoding='UTF-8').readlines()]
    return stopwords

#使用结巴分词分词
def seg_depart(sentence):
    #segment for each line
    sentence_depart = jieba.cut(sentence.strip())
    #word2vec算法依赖于上下文,而上下文有可能就是停用词,因此对于word2vec不要去停用词
    # stopwords = stopwordslist()
    # outstr = ""
    # for word in sentence_depart:
    #     if word not in stopwords:
    #         if word != ('/t' and "##"):
    #             outstr += word
    #             outstr += " "
    segment_res = ' '.join(sentence_depart)
    return segment_res

# 正则对字符串清洗
def textParse_news(str_doc):
    # 正则过滤掉特殊符号、标点、英文、数字等。
    r1 = '[0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    str_doc = re.sub(r1, ' ', str_doc)

    # 去掉字符
    str_doc = re.sub('\u3000', '', str_doc)

    # 去除空格
    str_doc=re.sub('\s+', ' ', str_doc)

    # 去除换行符
    #str_doc = str_doc.replace('\n',' ')
    return str_doc
