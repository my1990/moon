import numpy as np
import requests
requests.
plt.style.use('ggplot')
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = [u'中专',u'大专'u'本科',u'硕士']
explods = [0,0,1,0,0,0]
colores = ['#9999ff','#ff9999','#7777aa','2442aa','#dd5555']
plt.axes(aspect='equla')
plt.xlim(0,4)
plt.ylim(0,4)
plt.pie(
    x=edu,
    explods = explods,
    labels = labels,
    colores = colores,
    sutopct = '%.1f%%',
    pctdistance = 1.15,
    startangle = 180,
    radius = 1.5,
    counterclock = False,
    wedgeprops = {'linewidth':1.5,'edgecolor':'green'},
    textprops = {'fontsize':12,'color':'k'},
    center = (1,8,1,8),
    frame = 1
)

plt.xticks(())
plt.yticks(())
plt.title(u'ssss')
plt.show()