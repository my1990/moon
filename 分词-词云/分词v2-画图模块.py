#使用jieba模块 简单的分词
#结巴分词分为三种模式：精确模式（默认）、全模式和搜索引擎模式  https://www.cnblogs.com/jiayongji/p/7119065.html

import re,jieba
import jieba.posseg as psg
f = open('归去来兮辞.txt','r')
text = f.read()
f.close()

