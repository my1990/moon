numpy pandas等相关数据分析学习文件

余弦相似度算法
                     
  计算俩篇文章最常见的的就是利用余弦相似度算法了。关于余弦相似度是什么可以直接百度查看定义。我这里举一个例子来说明，用上述理论计算文本的相似性。为了简单起见，先从句子着手。

句子A：这只皮靴号码大了。那只号码合适

句子B：这只皮靴号码不小，那只更合适

怎样计算上面两句话的相似程度？

基本思路是：如果这两句话的用词越相似，它们的内容就应该越相似。因此，可以从词频入手，计算它们的相似程度。

第一步，分词。

句子A：这只/皮靴/号码/大了。那只/号码/合适。

句子B：这只/皮靴/号码/不/小，那只/更/合适。

第二步，列出所有的词。

这只，皮靴，号码，大了。那只，合适，不，小，很

第三步，计算词频。

句子A：这只1，皮靴1，号码2，大了1。那只1，合适1，不0，小0，更0

句子B：这只1，皮靴1，号码1，大了0。那只1，合适1，不1，小1，更1

第四步，写出词频向量。

　　句子A：(1，1，2，1，1，1，0，0，0)

　　句子B：(1，1，1，0，1，1，1，1，1)

到这里，问题就变成了如何计算这两个向量的相似程度。我们可以把它们想象成空间中的两条线段，都是从原点（[0, 0, ...]）出发，指向不同的方向。两条线段之间形成一个夹角，如果夹角为0度，意味着方向相同、线段重合,这是表示两个向量代表的文本完全相等；如果夹角为90度，意味着形成直角，方向完全不相似；如果夹角为180度，意味着方向正好相反。因此，我们可以通过夹角的大小，来判断向量的相似程度。夹角越小，就代表越相似。

使用上面的公式(4)

 ![](http://img.blog.csdn.net/20131111190818687)

计算两个句子向量

句子A：(1，1，2，1，1，1，0，0，0)

和句子B：(1，1，1，0，1，1，1，1，1)的向量余弦值来确定两个句子的相似度。

计算过程如下：

![](http://img.blog.csdn.net/20131111190905937)

计算结果中夹角的余弦值为0.81非常接近于1，所以，上面的句子A和句子B是基本相似的

由此，我们就得到了文本相似度计算的处理流程是:

    （1）找出两篇文章的关键词；

　（2）每篇文章各取出若干个关键词，合并成一个集合，计算每篇文章对于这个集合中的词的词频

　（3）生成两篇文章各自的词频向量；

　（4）计算两个向量的余弦相似度，值越大就表示越相似。

下面我们就用余弦相似度算法来比较《三国演义》和《西游记》俩本书的相似度。

```python
1、分词
import numpy as np
import math
import jieba.posseg as psg

def cut_word(name,max_number): #
    with open(name,'r',encoding='utf-8') as f:
        text = f.read()
    res2 = [(x.flag,x.word) for x in  psg.cut(text)]  #获取词性，如动词、名词等  w代表标点符号, x 代表字符串, p 介词（把、被）,  u 助词

    #利用词性去掉标点符号等词
    word_list = []  #分词结果
    word_dict = {} #词频结果

    for i in res2: #去掉标点符号等词
        if i[0] not in ['w','x','p','u']:
            word_list.append(i[1])

    for word in word_list:  #计算词频
        if len(word) != 1:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    sort_word = []  # 排序
    for word, freq in word_dict.items():
        sort_word.append((word, freq))
    sort_word.sort(key=lambda x: x[1], reverse=True)

    result = []
    for word, freq in sort_word[: max_number]:
        dict1 = {}
        dict1[word] = freq
        result.append(dict1)
    print(result)
    return result,len(word_list)



2、分词结束后，就是拿俩篇文章分词的结果去计算了，函数如下：
# num参数表示取去重后的多少个词，
def get_cos(page_1,page_2,num):
    A = cut_word(page_1,num)  #分词结果
    B = cut_word(page_2,num)
    if num > int(A[1]) or num > int(B[1]): #如果num值大于文章A的文词总数或者大于文章B的分词总数，就重新设置num，重新分词，
        if int(A[1]) <= int(B[1]):          
#比如num值为200，而文章A的分词总数为2000，文章B分词总数为20，这样得出的数组长度就不一致，会导致计算错，此时重新设置num值为20，重新给AB文章分词
            num = int(A[1])
            A = cut_word(page_1, num)  # 重新分词
            B = cut_word(page_2, num)
        else:
            num = int(B[1])
            A = cut_word(page_1, num)  # 重新分词
            B = cut_word(page_2, num)
    # print(A[0])
    # print(B[0])
    # A[0] 分词结果  A[0] 去重后词数  A[1] 未去重的总词数


    #把A[0] B[0] 字典形式各分成2个列表A_word存词  A_num 存该词出现的词数，方便后面计算
    A_word = []
    A_num = []
    B_word = []
    B_num = []
    for info_A in A[0]:
        for key_A in info_A:
            A_word.append(key_A)
            A_num.append(info_A[key_A])
    for info_B in B[0]:
        for key_B in info_B:
            B_word.append(key_B)
            B_num.append(info_B[key_B])
    list_A = []  #文章A的向量值
    list_B = []
    for word_A in A_word:  
#A文章出现频率高的词，拿出现次数 / 本篇文章总次数当做权重值，再拿权重值 * 该词在另一篇文章中出现的次数，结果存在list_1中做向量用
        num_A = A_num[A_word.index(word_A)] / A[2]  #权重值 = 词出现次数 / 总词数
        if B_word.count(word_A) == 1:  #如果A 文章的词出现在B文章，就取出现次数
            count = B_num[B_word.index(word_A)]
            list_A.append(num_A * count)
        else:                        #如果A 文章的词没有出现在B文章，conut就是0
            count = 0
            list_A.append(num_A * count)
    for word_B in B_word:  
#B文章出现频率高的词，拿出现次数 / 本篇文章总次数当做权重值，再拿权重值 * 该词在另一篇文章中出现的次数，结果存在list_1中做向量用
        num_B = B_num[B_word.index(word_B)] / B[2]  #权重值 = 词出现次数 / 总词数
        if A_word.count(word_B) == 1:  #如果B 文章的词出现在A文章，就取出现次数
            count = A_num[A_word.index(word_B)]
            list_B.append(num_B * count)
        else:                        #如果B 文章的词没有出现在A文章，conut就是0
            count = 0
            list_B.append(num_B * count)

    arr1 = np.array(list_A) #列表转数组
    arr2 = np.array(list_B)
    #余弦相似度公式
    M = (arr1 * arr2).sum()
    P1 = (arr1 * arr1).sum()
    P2 = (arr2 * arr2).sum()

    Q = math.sqrt(P1)
    W = math.sqrt(P2)

    cos = M / (Q * W)
    cos1 = "%.2f%%" % (cos*100)
    print("%s文章与%s文章相似度为：%s " % (page_1,page_2,cos1))

#调用函数
name1 = '三国演义.txt'
name2 = '西游记.txt'
get_cos(name1,name2,2000)

#结果如下：
三国演义.txt文章与西游记.txt文章相似度为：35.41%

```
-----------------------------------------------------------------------------------

