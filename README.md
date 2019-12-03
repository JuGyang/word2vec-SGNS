# 基于Skip-Gram with Negative Sampling(SGNS)的汉语词向量学习和评估

## 1. 实验要求

* 一 词向量学习
超参数:前后两窗口,维数:100
训练语料：https://dumps.wikimedia.org/backup-index.html  汉语数据
* 二、词向量评估
采用所学得的词向量，计算pku_sim_test.txt文件中每行两个词间的余弦距离作为两词相似度，并输出到文件中。输出要求如下，因为是机器判定，请一定按如下格式输出，否者可能得到不好的判定结果：
1)输出文件的编码： utf-8
2)输出格式：词之间以及词和相似度之间使用一个tab符分开，如下例：
没戏	没辙	4.3
3)不要打乱pku_sim_test.txt中原来的行序，当pku_sim_test.txt中的某个词没有词向量时，对应的该行的词间相似度标识为OOV，即，如果没有“没辙”这个词的词向量，则对应的行输出为：
没戏	没辙	OOV
4)输出文件以自己的学号命名

## 2. 实验步骤
### 2.1 parse_zhwiki_corpus.py 将zhwiki.xml转化成zhwiki.txt格式
### 2.2 traditional2simplified.py 将zhwiki.txt中的繁体字转化为简体字
### 2.3 zhWiki_seg.py 清洗数据并分词
### 2.4 word2vec_train.py 训练word2vec模型
### 2.5 word2vec_test.py 测试word2vec模型

## 3. 参考与致谢
1. https://www.jianshu.com/p/6a34929c165e
2. https://www.cnblogs.com/pinard/p/7160330.html
