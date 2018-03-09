'''
wordcloud包的基本用法
font_path : string //字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
width : int (default=400) //输出的画布宽度，默认为400像素
height : int (default=200) //输出的画布高度，默认为200像素
prefer_horizontal : float (default=0.90) //词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）
mask : nd-array or None (default=None) //如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。
                                            除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，
                                            背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布上再保存，就ok了。
scale : float (default=1) //按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
min_font_size : int (default=4) //显示的最小的字体大小
font_step : int (default=1) //字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
max_words : number (default=200) //要显示的词的最大个数
stopwords : set of strings or None //设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
background_color : color value (default=”black”) //背景颜色，如background_color='white',背景颜色为白色。
max_font_size : int or None (default=None) //显示的最大的字体大小
mode : string (default=”RGB”) //当参数为“RGBA”并且background_color不为空时，背景为透明。
relative_scaling : float (default=.5) //词频和字体大小的关联性
color_func : callable, default=None //生成新颜色的函数，如果为空，则使用 self.color_func
regexp : string or None (optional) //使用正则表达式分隔输入的文本
collocations : bool, default=True //是否包括两个词的搭配
colormap : string or matplotlib colormap, default=”viridis” //给每个单词随机分配颜色，若指定color_func，则忽略该方法。
'''
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.misc import imread
from os import path

f = open('梦里花落知多少.txt','r',encoding='utf-8')
text = f.read()
f.close()
d = path.dirname(__file__)
cut_text = ' '.join(jieba.cut(text))
color_mask = imread("C:\\Users\\Administrator\\Downloads\\20160721185925416.jpg") # 读取背景图片
cloud = WordCloud(font_path='./STXINGKA.TTF',background_color='white',mask=color_mask,max_words=800,max_font_size=80)
word_cloud = cloud.generate(cut_text) # 产生词云
word_cloud.to_file("pjl_cloud.jpg")

