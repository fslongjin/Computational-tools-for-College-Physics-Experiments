import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0.0, 1.5, 1000)
y = 1/(2*x)

# 设置图像大小
plt.figure(num=3, figsize=(15, 10))

# 绘图
plt.plot(x, y, color='red', linewidth=1.0, linestyle='-')

# 设置坐标轴标签、范围
plt.xlim(0, 1)
plt.ylim(0, 15)
plt.xlabel('x')
plt.ylabel('y')

# 设置刻度范围及数量
new_ticks = np.linspace(0, 1.5, 10)

plt.xticks(new_ticks)
y_ticks = np.linspace(0, 10, 20)
plt.yticks(y_ticks)

# 获取坐标轴信息
ax = plt.gca()


# 使用.spines设置边框；将右边颜色设置为None
# 使用set_position设置边框位置：y=0的位置  位置所有属性：outward，axes，data）
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#移动坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

#将y坐标轴移动到x=0的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 设置标签
ax.set_title('xy=1/2', fontsize=14, color='r')

plt.show()

