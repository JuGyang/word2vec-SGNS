
# Description:输出文件中两个词的余弦距离
# Author：Yang Jiang
# Prompt: code in Python3 env
#

import os
import logging
import pprint
import sys
import time
import json
from gensim.models import Word2Vec
from const import model_dir, cache_dir, data_dir
from optparse import OptionParser


def word2vec_test(input_file, output_file, path_Word2Vec_Model, path_Word2Vec_Vec):
    word2vec_model = Word2Vec.load(path_Word2Vec_Model)
    sim_test = []
    for each in range(500):
        sim_test.append([])
    #用于生成一个词典,词典记录了有向量的字段,如果没有将结果置为OOV
    print("===正在生成字典===")
    dictionary = []
    with open(path_Word2Vec_Vec, 'r') as fin_vec:
        for line in fin_vec:
            line = line.replace('.', ' ').replace(',', ' ').strip()
            dictionary.append(line.split()[0])
    with open(os.path.join(cache_dir, 'dict.json'),'w') as fout_vec:
           json.dump(dictionary, fout_vec)
    print("===字典已生成===")
    with open(os.path.join(cache_dir, 'dict.json'),'r') as f:
        dict = json.load(f)
    with open(input_file, 'r', encoding='utf-8') as fin:
        i = 0
        for line in fin:
            str_tmp1, str_tmp2 = line.split('\t', 1)
            str1 = str_tmp1
            str2 = str_tmp2.replace('\n', '')
            if (str1 not in dict) or (str2 not in dict):
                sim_test[i].append((str1, str2, 'OOV'))
                print(str1 + '\t' + str2 + '\t' +'OOV')
            else:
                sim = word2vec_model.wv.similarity(str1, str2)
                print(str1 + '\t' + str2 + '\t' + str(sim))
                sim_test[i].append((str1, str2, str(sim)))
            i += 1
    with open(output_file, 'w', encoding='utf-8') as fout:
        for each in sim_test:
            fout.writelines(str(each[0][0]) + '\t'+ str(each[0][1]) + '\t'+ str(each[0][2]) + '\n')


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program)  # logging.getLogger(logger_name)
    logger.info('running ' + program + ': convert Traditional Chinese to Simplified Chinese')

    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_file',
    default=os.path.join(data_dir, 'pku_sim_test.txt'), help='input:test file')
    parser.add_option('-o', '--output', dest='output_file',
    default=os.path.join(cache_dir, '2019140499'), help='output:test file with similaraties')
    parser.add_option('-m', '--inmodel', dest='path_Word2Vec_Model',
    default=os.path.join(model_dir, 'zhwiki.word2vec.model'), help='input: path to word2vec model')
    parser.add_option('-v', '--invec', dest='path_Word2Vec_Vec',
    default=os.path.join(model_dir, 'zhwiki.word2vec.vectors'), help='input: path to word2vec vec')



    (options, args) = parser.parse_args()

    input_file = options.input_file
    output_file = options.output_file
    path_Word2Vec_Model = options.path_Word2Vec_Model
    path_Word2Vec_Vec = options.path_Word2Vec_Vec


    try:
        start = time.time()
        word2vec_test(input_file, output_file, path_Word2Vec_Model, path_Word2Vec_Vec)
        end = time.time()
        print('total spent times:%.2f' % (end-start)+ ' s')
    except Exception as err:
        logger.info(err)
