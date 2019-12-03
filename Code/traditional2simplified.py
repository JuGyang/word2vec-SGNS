
# Description:将zhwiki.txt中的繁体字转化为简体字
# Author：Yang Jiang
# Prompt: code in Python3 env


import os
import sys
import time
import logging
from optparse import OptionParser
from opencc import OpenCC
from const import cache_dir

def zh_tr2simp(input_file, output_file):
    #读取zhwiki.txt
    zh_tr_corpus = []
    with open(input_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            line = line.replace('\n', '').replace('\n', '')
            zh_tr_corpus.append(line)
    logger.info('read traditional file finished!')

    #将繁体字转化成简体字
    cc = OpenCC('t2s')
    zh_simp = []
    for i,line in zip(range(len(zh_tr_corpus)), zh_tr_corpus):
        if i%1000 == 0:
            logger.info(' *** {i} \t docs has been dealed'.format(i=i))
        zh_simp.append(cc.convert(line))
    logger.info('convert t2s finished!')

    #将简体字写入corpus.zhwiki_simplified.txt
    with open(output_file, 'w', encoding='utf-8') as fout:
        for line in zh_simp:
            fout.writelines(line + '\n')
    logger.info('write simplified file finished!')

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program)  # logging.getLogger(logger_name)
    logger.info('running ' + program + ': convert Traditional Chinese to Simplified Chinese')

    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_file',
    default=os.path.join(cache_dir, 'corpus.zhwiki.txt'), help='input:traditional file')
    parser.add_option('-o', '--output', dest='output_file',
    default=os.path.join(cache_dir, 'corpus.zhwiki.simplified.txt'), help='output:simplified file')

    (options, args) = parser.parse_args()

    input_file = options.input_file
    output_file = options.output_file

    try:
        start = time.time()
        zh_tr2simp(input_file, output_file)
        end = time.time()
        print('total spent times:%.2f' % (end-start)+ ' s')
    except Exception as err:
        logger.info(err)
