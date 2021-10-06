from numpy.core.fromnumeric import _repeat_dispatcher, repeat
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
import ipdb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
file_name = 'foryou_data.xlsx'

df = pd.read_excel(file_name)
cols = df.shape[1]

df['日期文本'] = df['日期'].apply(lambda x: str(x)[:10])
t = datetime.datetime(2021,3,15) # 起始日期
now_str = datetime.datetime.now().strftime('%Y-%m-%d')
now = datetime.datetime.strptime(now_str, "%Y-%m-%d")
begin = datetime.datetime.strptime("2021-3-15", "%Y-%m-%d")
date_time = (now- begin).days

fig, ax = plt.subplots(figsize=(10,6)) # 画布

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 字体设为微软雅黑
timeSlot = [x for x in range(0,date_time)] # 时间轴
colors = ['#ADD8E6', '#DC143C', '#FFC0CB', '#DFD7D7']  # 颜色列表


def draw(date):
   # print(date)
    # 数据处理 ------
    current_date = (t + datetime.timedelta(days=date)).strftime("%Y-%m-%d")
    df_ = df[df['日期文本'].eq(current_date)]
   # ipdb.set_trace()
 #   ipdb.set_trace()
    days = [int(df_['天数'].values[0])]
    
    items = [df_["项目"].values[0]]
    for j in range(1, int(cols/3) ):
        if (df_['天数.{}'.format(j)].values) != df_['天数.{}'.format(j)].values: # check nan
           
            break
        else:
            days.append(int(df_['天数.{}'.format(j)].values[0]))
            items.append(df_["项目.{}".format(j)].values[0])
    # 绘制条形图 ------
  #  ipdb.set_trace()
    ax.clear() # 重绘
    ax.barh(items, days, color = colors)
    for y, (x,name) in enumerate(zip(days,items)): # 系列标注
            ax.text(x, y, "%s天" % x, size=16)
            if x > 1:
                ax.text(x, y, name, size=16, ha = 'right')
    ax.text(1, 1.01, current_date, transform = ax.transAxes, size= 20, ha='right') # 滚动时间
    ax.get_xaxis().set_visible(False) # 隐藏坐标轴
    ax.get_yaxis().set_visible(False)

#draw(100)
#plt.savefig('test.png')
animator = ani.FuncAnimation(fig, draw, frames=timeSlot ,interval = 80, repeat_delay = 2000) # interval时间间隔

animator.save('test.gif',fps=10)