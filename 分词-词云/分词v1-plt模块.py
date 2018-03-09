from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.misc import imread
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
f = open('梦里花落知多少.txt','r',encoding='utf-8')
text = f.read()
f.close()

d = path.dirname(__file__)

cut_text = ' '.join(jieba.cut(text))

color_mask = imread("C:\\Users\\Administrator\\Downloads\\20160721185925416.jpg") # 读取背景图片
cloud = WordCloud(font_path='./STXINGKA.TTF',background_color='white',mask=color_mask,max_words=800,max_font_size=80)
word_cloud = cloud.generate(cut_text) # 产生词云


image_colors = ImageColorGenerator(color_mask)

plt.figure()
# 以下代码显示图片
plt.imshow(cloud)
plt.axis("off")
plt.show()
# 绘制词云

# 保存图片
cloud.to_file(path.join(d, "名称.png"))
