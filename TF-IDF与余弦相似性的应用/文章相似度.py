'''
计算A、B俩篇文章相似度
1、先给A B分词 得出出现频率高的前N个词组
2、计算文章向量值list
'''
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
    #print(result)
    return result,len(word_list)

def get_cos(page_1,page_2,num):
    A = cut_word(page_1,num)  #分词结果
    B = cut_word(page_2,num)
    word_all = int(A[1]) + int(B[1])  #俩篇文章所有词数的和

    list_A = []  #文章A的向量值
    list_B = []
    for info in A[0]:  #A文章出现频率高的词，拿出现次数 / 俩篇文章总次数，结果存在list_1中做向量用
        for key in info:
            num_A = info[key] / word_all
            list_A.append(num_A)
    for info in B[0]: #B文章出现频率高的词，拿出现次数 / 俩篇文章总次数，结果存在list_2中做向量用
        for key in info:
            num_B = info[key] / word_all
            list_B.append(num_B)

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


name1 = '三国演义.txt'
name2 = '西游记.txt'
get_cos(name1,name2,2000)
