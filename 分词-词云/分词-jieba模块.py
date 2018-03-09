#使用jieba模块 简单的分词
#结巴分词分为三种模式：精确模式（默认）、全模式和搜索引擎模式  https://www.cnblogs.com/jiayongji/p/7119065.html

import re,jieba
import jieba.posseg as psg
f = open('梦里花落知多少.txt','r',encoding='utf-8')
text = f.read()
f.close()
search_str = '我'
count = len(re.findall(search_str,text))
print('字符串:"%s" 共计出现%s次！' % (search_str,count))

res1 = jieba.lcut(text)  #整体分词
res2 = [(x.flag,x.word) for x in  psg.cut(text)]  #获取词性，如动词、名词等  w代表标点符号, x 代表字符串, p 介词（把、被）,  u 助词
#利用词性去掉标点符号等词
list = []
for i in res2: #去掉标点符号等词
    if i[0] not in ['w','x']:
        list.append(i[1])

#排序  词频
list1 = []
for i in res2:
    if i[0] not in ['w','x','p','u']: #去掉标点符号 字符串 介词和助词
        list1.append(i[1])
word_freq = {}
for word in list1:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)

print(freq_word)
list2 = []
for i in freq_word:
    if len(i[0]) != 1:
        list2.append(i)
max_number = 20
for word, freq in list2[: max_number]:
    print (word, freq)

