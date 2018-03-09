#http://blog.csdn.net/cdnight/article/details/48468653


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  #linspac 方法是从0-10中产生100个数
y = np.sin(x)
z = np.cos(x)
plt.figure(figsize=(8,4))   #调用figure创建一个绘图对象，并且使它成为当前的绘图对象,整个图像就是一个figure对象
                            #figsize参数可以指定绘图对象的宽度和高度，单位为英寸；
                            # dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80。因此本例中所创建的图表窗口的宽度为8*80 = 640像素

#下面的两行程序通过调用plot函数在当前的绘图对象中进行绘图
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x)$")

'''
plot函数的调用方式很灵活，第一句将x,y数组传递给plot之后，用关键字参数指定各种属性：
label : 给所绘制的曲线一个名字，此名字在图示(legend)中显示。只要在字符串前后添加"$"符号，
        matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
color : 指定曲线的颜色
linewidth : 指定曲线的宽度
第二句直接通过第三个参数"b--"指定曲线的颜色和线型，这个参数称为格式化参数，它能够通过一些易记的符号快速指定曲线的样式。
其中b表示蓝色，"--"表示线型为虚线。在IPython中输入 "plt.plot?" 可以查看格式化字符串的详细配置。
'''

#接下来通过一系列函数设置绘图对象的各个属性
plt.xlabel("Time(s)")      #设置X轴的文字
plt.ylabel("Volt")         #设置Y轴的文字
plt.title("ssssssssss")   #设置图表的标题
plt.ylim(-100,100,5,5)          #设置Y轴的范围,第一个值表示y轴最小数，第二个值表示y轴最大数
plt.xlim(-100,100,5)                 #设置X轴范围
plt.legend()                #显示图示
plt.show()                  #最后调用plt.show()显示出我们创建的所有绘图对象

# 将当前figure的图保存到文件result.png
plt.savefig('result.png')