
# Description:训练Word2Vec模型
# Author：Yang Jiang
# Prompt: code in Python3 env


import os
import sys
import multiprocessing
import logging
from optparse import OptionParser
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from const import cache_dir, model_dir

#用于对wiki_zh进行Word2vec模型的训练
def word2vec_train(input_file, outmodel, outvector, size, window,sg, hs, min_count):
    #size:词向量的维度
    #window:词向量上下文最大距离
    #sg：word2vec两个模型的选择（0：CBOW，1：Skip-Gram）（default=0）
    #hs：word2vec两个解法的选择（0：Negative Sampling，1：Hierarchical Softmax *若置1，则negative需要大于0）（default=0）
    #min_count：需要计算词向量的最小词频（default=5）

    #train model
    model = Word2Vec(LineSentence(input_file), size=size, window=window,
    sg = sg, hs = hs,
    min_count=min_count, workers=multiprocessing.cpu_count())

    #save model
    model.save(outmodel)
    model.wv.save_word2vec_format(outvector, binary=False)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program)

    logger.info('running ' + program)

    # parse the parameters
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_file', default=os.path.join(cache_dir, 'corpus.zhwiki.simplified.segment.txt'), help='zhwiki corpus')
    parser.add_option('-m', '--outmodel', dest='wv_model', default=os.path.join(model_dir, 'zhwiki.word2vec.model'), help='word2vec model')
    parser.add_option('-v', '--outvec', dest='wv_vectors', default=os.path.join(model_dir, 'zhwiki.word2vec.vectors'), help='word2vec vectors')
    parser.add_option('-s', type='int', dest='size', default=100, help='word vector size')
    parser.add_option('-w', type='int', dest='window',default=2, help='window size')
    parser.add_option('--sg', type='int', dest='sg', default=1, help='0:CBOW 1:Skip-Gram')
    parser.add_option('--hs', type='int', dest='hs', default=0, help='0:Negative Sampling 1:Hierarchical Softmax')
    parser.add_option('-n', type='int', dest='min_count', default=5, help='min word frequency')

    (options,argv) = parser.parse_args()
    input_file = options.input_file
    outmodel = options.wv_model
    outvector = options.wv_vectors
    size = options.size
    window = options.window
    sg = options.sg
    hs = options.hs
    min_count = options.min_count

    try:
        word2vec_train(input_file, outmodel, outvector, size, window,sg, hs, min_count)
        logger.info('word2vec model training finished')
    except Exception as err:
        logger.info(err)
