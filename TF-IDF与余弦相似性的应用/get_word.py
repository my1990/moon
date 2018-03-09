#http://www.ruanyifeng.com/blog/2013/03/tf-idf.html
#  TF-IDF算法-提取文本关键字
# TF  "词频"（Term Frequency，缩写为TF）
# IDF "逆文档频率"（Inverse Document Frequency，缩写为IDF）
# 知道了"词频"（TF）和"逆文档频率"（IDF）以后，将这两个值相乘，就得到了一个词的TF-IDF值。某个词对文章的重要性越高，它的TF-IDF值就越大。所以，排在最前面的几个词，就是这篇文章的关键词。
import requests,time,re
from bs4 import BeautifulSoup
import math,jieba
import jieba.posseg as psg

# 计算词频 词频表示词在文中出现的次数。  等于某个词出现次数/总词数
def get_TF(name,max_number):
    with open(name,'r',encoding='utf-8') as f:
        text = f.read()
    res2 = [(x.flag,x.word) for x in  psg.cut(text)]  #获取词性，如动词、名词等  w代表标点符号, x 代表字符串, p 介词（把、被）,  u 助词
    #利用词性去掉标点符号等词
    word_list = []  #分词结果
    unique_list = [] #词语唯一性结果
    word_dict = {} #词频结果

    for i in res2: #去掉标点符号等词
        if i[0] not in ['w','x','p','u']:
            word_list.append(i[1])

    for word in word_list:  #计算词频
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sort_word = []  #排序
    for word, freq in word_dict.items():
        sort_word.append((word, freq))
    sort_word.sort(key=lambda x: x[1], reverse=True)

    word_list_1 = []  #去掉词是单个字的，比如 的 呢 了
    for i in sort_word:
        if len(i[0]) != 1:
            word_list_1.append(i)


    TF_resule = {} #最终的词的词频
    for word, num in word_list_1[: max_number]:
        TF = int(num) / int(len(word_list))
        TF_resule[word] = TF

    return TF_resule



#计算逆文档频率,百度最多只显示100,000,000个结果，所有假设百度文档最多有1,000,000,000个文档
def search_result(search_str):
    url = 'http://www.baidu.com/s?wd=' + search_str + '&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'

    data = requests.get(url).text
    soup = BeautifulSoup(data,'lxml')
    #title = soup.select(".c-container h3 a")
    num = re.findall(r'百度为您找到相关结果约(.*?)个',data)[0].replace(',','') #某个词搜索到的结果条数

    return num




#name  需要分词的文件名  max_number  提取前多少个词
def main(name,max_number):
    TF_result = get_TF(name,max_number)
    word_TF_IDF_result = {} #词TF-IDF
    for word,TF in TF_result.items():
        num = search_result(word)   #某个词百度搜索结果的条数
        IDF = math.log(int(1000000000) / (int(num) + 1))   #词的IDF
        word_TF_IDF = TF * IDF  #计算TF-IDF
        word_TF_IDF_result[word] = word_TF_IDF
    # print(word_TF_IDF_result)
    #排序
    reult = []
    for word1, TF_IDF in word_TF_IDF_result.items():
        reult.append((word1, TF_IDF))
        reult.sort(key=lambda x: x[1], reverse=True)
    # for i in reult:
    #     print(i)
    print(reult)
    return reult


#name = '梦里花落知多少.txt'
name = '《草房子》完整版.txt'
main(name,20)