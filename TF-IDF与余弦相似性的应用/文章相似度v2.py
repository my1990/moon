'''
计算A、B俩篇文章相似度
1、先给A B分词 得出出现频率高的前N个词组
2、计算文章向量值list
'''
import numpy as np
import math,jieba
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

    result = [] #最终分词结果
    for word, freq in sort_word[: max_number]:
        dict1 = {}
        dict1[word] = freq
        result.append(dict1)
    # print(len(result),result)
    # print(len(word_list))
    return result,len(result),len(word_list)#result 是分词结果信息，len(result)是文章共有多少种词，去重过的结果，len(word_list)是分词结果，共有多少个词，未去重

# num参数表示取去重后的多少个词，
def get_cos(page_1,page_2,num):
    A = cut_word(page_1,num)  #分词结果
    B = cut_word(page_2,num)
    if num > int(A[1]) or num > int(B[1]): #如果num值大于文章A的文词总数或者大于文章B的分词总数，就重新设置num，重新分词，
        if int(A[1]) <= int(B[1]):          # 比如num值为200，而文章A的分词总数为2000，文章B分词总数为20，这样得出的数组长度就不一致，会导致计算错，此时重新设置num值为20，重新给AB文章分词
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
    for word_A in A_word:  #A文章出现频率高的词，拿出现次数 / 本篇文章总次数当做权重值，再拿权重值 * 该词在另一篇文章中出现的次数，结果存在list_1中做向量用
        num_A = A_num[A_word.index(word_A)] / A[2]  #权重值 = 词出现次数 / 总词数
        if B_word.count(word_A) == 1:  #如果A 文章的词出现在B文章，就取出现次数
            count = B_num[B_word.index(word_A)]
            list_A.append(num_A * count)
        else:                        #如果A 文章的词没有出现在B文章，conut就是0
            count = 0
            list_A.append(num_A * count)
    for word_B in B_word:  #B文章出现频率高的词，拿出现次数 / 本篇文章总次数当做权重值，再拿权重值 * 该词在另一篇文章中出现的次数，结果存在list_1中做向量用
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


name1 = '三国演义.txt'
name2 = '西游记.txt'
get_cos(name1,name2,200000)