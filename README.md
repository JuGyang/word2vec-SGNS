# 基于Skip-Gram with Negative Sampling(SGNS)的汉语词向量学习和评估

## 1. 实验要求

### 1.1 词向量学习
超参数:前后两窗口,维数:100
训练语料：https://dumps.wikimedia.org/backup-index.html  汉语数据
### 1.2 词向量评估
采用所学得的词向量，计算pku_sim_test.txt文件中每行两个词间的余弦距离作为两词相似度，并输出到文件中。输出要求如下，因为是机器判定，请一定按如下格式输出，否者可能得到不好的判定结果：  
1)输出文件的编码： utf-8  
2)输出格式：词之间以及词和相似度之间使用一个tab符分开，如下例：
没戏	没辙	4.3  
3)不要打乱pku_sim_test.txt中原来的行序，当pku_sim_test.txt中的某个词没有词向量时，对应的该行的词间相似度标识为OOV，即，如果没有“没辙”这个词的词向量，则对应的行输出为：
没戏	没辙	OOV  
4)输出文件以自己的学号命名

### 2. 实验环境

* Python3.7  
* jieba、gensim、opencc


## 3. 实验步骤
### 3.1 中文语料
本次实验采用维基百科的中文语料库训练word2vec模型
### 3.2 parse_zhwiki_corpus.py 将zhwiki.xml转化成zhwiki.txt格式
使用gensim包的WikiCorpus方法将zhwiki*.xml.bz2文件转化为corpus.zhwiki.txt  
使用命令
```
python3 parse_zhwiki_corpus.py -i input_file -o output_file
```
### 3.3 traditional2simplified.py 将zhwiki.txt中的繁体字转化为简体字
将zh_wiki*.xml.bz2 转化为 corpus_zhwiki.txt 后发现，语料中带有大量的繁体字，所以使用opencc库将繁体字转化为简体字  
使用命令  
```
python3 traditional2simplified.py -i input_file -o output_file
```
### 3.4 zhWiki_seg.py 清洗数据并分词

进入清洗数据阶段，数据预处理过程详情请点击：https://weibo.com/ttarticle/p/show?id=2309404444679423787160

因为word2vec是通过上下文来训练，所以不需要去停用词，这里使用正则表达式去掉一些特殊字符，并使用jieba进行分词

使用命令
```
python3 zhWiki_seg.py -i input_file -o output_file
```
### 3.5 word2vec_train.py 训练word2vec模型

这里使用gensim的word2vec方法进行训练，这里提供了一些参数供训练，列出一些重要的参数  
* size:词向量的维度
* window:词向量上下文最大距离
* sg：word2vec两个模型的选择（0：CBOW，1：Skip-Gram）（default=0）
* hs：word2vec两个解法的选择（0：Negative Sampling，1：Hierarchical Softmax *若置1，则negative需要大于0）（default=0）
* min_count：需要计算词向量的最小词频（default=5）

使用命令
```
python3 word2vec_train.py -i input_file -m out_model -v out_vector
```

### 3.6 word2vec_test.py 测试word2vec模型

在测试环节中，我们使用pku_sim_test.txt进行测试，进行两个词词向量的余弦距离计算  
这里使用word2vec_model.wv.similarity方法  
*发现当词没有词向量时，使用word2vec_model.wv.similarity会报错，这里使用一个技巧，生成一个字典，首先检测词是否出现在字典中，然后当该词没有词向量的使用，就会输出OOV，程序就不会报错了（消耗了时间，但是暂时没想到其他方法）

使用命令
```
python3 word2vec_test.py -i input_file -o output_file
```
### 3.7 后期调参

后期具体调参详情，可点击链接： https://weibo.com/ttarticle/p/show?id=2309404444296089567296


## 4. 参考与致谢
1. https://www.jianshu.com/p/6a34929c165e
2. https://www.cnblogs.com/pinard/p/7160330.html

再次感谢各位大佬!
