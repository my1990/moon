import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=16)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = [1,2,3,4,5,6,7,8,9]  #linspac 方法是从0-10中产生100个数
y = np.sin(x)
z = np.cos(x)
# b = np.math(0)
#plt.figure(figsize=(8,4))   #调用figure创建一个绘图对象，并且使它成为当前的绘图对象,整个图像就是一个figure对象
                            #figsize参数可以指定绘图对象的宽度和高度，单位为英寸；
                            # dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80。因此本例中所创建的图表窗口的宽度为8*80 = 640像素

#下面的两行程序通过调用plot函数在当前的绘图对象中进行绘图
#每一个plot就是一个函数
plt.plot([x/2 for x in x],color='red',label='f(x)=x')
plt.plot([0.5 for x in x],color='yellow')

#接下来通过一系列函数设置绘图对象的各个属性
plt.xlabel("这是X轴啊 看清楚了")      #设置X轴的文字
plt.ylabel("我是Y轴啊")         #设置Y轴的文字
plt.title("此处为标题")   #设置图表的标题
plt.ylim(0,1,10)          #设置Y轴的范围,第一个值表示y轴最小数，第二个值表示y轴最大数
plt.xlim(0,2,10)                 #设置X轴范围
#添加标注
plt.annotate('标注',xy=(1,0.5),xytext=(1,0.6),arrowprops=dict(facecolor='black'))
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(0.2,0.8), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.legend()                #显示图示
plt.show()                  #最后调用plt.show()显示出我们创建的所有绘图对象



