
# Description:将中文简体Wiki使用正则表达式清洗,并分词
# Author：Yang Jiang
# Prompt: code in Python3 env

import re
import jieba
import sys
import os
import logging
import time
from optparse import OptionParser

from const import common_dir, cache_dir
from regular_expression import *

# 可以直接调用这个函数进行清洗符号空格及分词
def pretreat_doc(str_doc):
    str_doc = textParse_news(str_doc)
    str_doc = seg_depart(str_doc)
    return str_doc

def zhwiki_seg(input_file, output_file):
    #读取zhwiki文件
    zhwiki_simplified_corpus = []
    with open(input_file, 'r') as fin:
        for line in fin:
            zhwiki_simplified_corpus.append(line)
    logging.info('read zhwiki finished!')

    #将zhwiki分词
    zhwiki_corpus_seg = []
    with open(output_file, 'w') as fout:
        for i, line in  zip(range(len(zhwiki_simplified_corpus)), zhwiki_simplified_corpus):
            if i%1000 == 0:
                logging.info(' *** {i} \t docs has been dealed'.format(i=i))
            zhwiki_corpus_seg.append(pretreat_doc(line))
    logging.info('zhwiki segment finished!')

    #写入文件zhwiki_corpus_simplified_seg.txt文件中
    with open(output_file, 'w', encoding='utf-8') as fout:
        for line in zhwiki_corpus_seg:
            fout.writelines(line + '\n')
    logging.info('write zhwiki segment finished!')

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program)  # logging.getLogger(logger_name)
    logger.info('running ' + program + ': zhWiki segment')

    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_file',
    default=os.path.join(cache_dir, 'corpus.zhwiki.simplified.txt'), help='input:simplified file')
    parser.add_option('-o', '--output', dest='output_file',
    default=os.path.join(cache_dir, 'corpus.zhwiki.simplified.segment.txt'), help='output:simplified segment file')

    (options, args) = parser.parse_args()

    input_file = options.input_file
    output_file = options.output_file

    try:
        start = time.time()
        zhwiki_seg(input_file, output_file)
        end = time.time()
        print('total spent times:%.2f' % (end-start)+ ' s')
    except Exception as err:
        logger.info(err)
