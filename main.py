from numpy.core.fromnumeric import _repeat_dispatcher, repeat
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
import ipdb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
# file_name = './data/foryou_data.xlsx'

# df = pd.read_excel(file_name)
# cols = df.shape[1]

item0 = {'project':'相遇', 'date':datetime.datetime.strptime('2021-3-15', "%Y-%m-%d")}
item1 = {'project':'我们在一起', 'date':datetime.datetime.strptime('2021-3-30', "%Y-%m-%d")}
item2 = {'project':'第一次相拥而眠','date':datetime.datetime.strptime('2021-5-20', "%Y-%m-%d")}
item3 = {'project':'第一次一起旅行', 'date':datetime.datetime.strptime('2021-9-18', "%Y-%m-%d")}
all_items = [item0, item1,item2, item3]

#df['日期文本'] = df['日期'].apply(lambda x: str(x)[:10])
t = datetime.datetime(2021,3,15) # 起始日期
now_str = datetime.datetime.now().strftime('%Y-%m-%d')
now = datetime.datetime.strptime(now_str, "%Y-%m-%d")
begin = datetime.datetime.strptime("2021-3-15", "%Y-%m-%d")
date_time = (now- begin).days + 1

fig, ax = plt.subplots(figsize=(10,6)) # 画布

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 字体设为微软雅黑

timeSlot = [x for x in range(0,date_time)] # 时间轴
colors = ['#ADD8E6', '#DC143C', '#FFC0CB', '#DFD7D7']  # 颜色列表


def draw(date):
   # print(date)
    # 数据处理 ------
    current_date_str = (t + datetime.timedelta(days=date)).strftime("%Y-%m-%d")
    current_date = t + datetime.timedelta(days=date)
    # df_ = df[df['日期文本'].eq(current_date)]
    
    # days = [int(df_['天数'].values[0])]
    
    # items = [df_["项目"].values[0]]
    # for j in range(1, int(cols/3) ):
    #     if (df_['天数.{}'.format(j)].values) != df_['天数.{}'.format(j)].values: # check nan
    #         break
    #     else:
    #         days.append(int(df_['天数.{}'.format(j)].values[0]))
    #         items.append(df_["项目.{}".format(j)].values[0])
    # # 绘制条形图 ------
    items =[all_items[0]['project']]
    days = [(current_date - t).days]
    for j in range(1, len(all_items)):
        day = (current_date - all_items[j]['date']).days + 1
        if  day > 0:
            items.append(all_items[j]['project'])
            days.append(day)

    ax.clear() # 重绘
    ax.barh(items, days, color = colors)
    ax.set_title("老高(^^)/ 和 \(^^)小涵", fontsize = 25 )
    for y, (x,name) in enumerate(zip(days,items)): # 系列标注
            ax.text(x, y, "%s天" % x, size=16)
            if x > 1:
                ax.text(x, y, name, size=16, ha = 'right')
    ax.text(1, 1.01, current_date_str, transform = ax.transAxes, size= 20, ha='right') # 滚动时间
    ax.get_xaxis().set_visible(False) # 隐藏坐标轴
    ax.get_yaxis().set_visible(False)

#draw(100)
#plt.savefig('test.png')
animator = ani.FuncAnimation(fig, draw, frames=timeSlot + [timeSlot[-1]] *20 ,interval = 80, repeat_delay = 2000) # interval时间间隔

animator.save('./data/test.gif',fps=8, savefig_kwargs={'bbox_inches':'tight'})