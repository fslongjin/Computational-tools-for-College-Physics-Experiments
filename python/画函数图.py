import matplotlib.pyplot as plt

import numpy as np


x = np.linspace(-5, 5, 1000000)
y = np.sqrt(2*x - x**2)




# 设置图像大小
plt.figure(num=3, figsize=(10, 10))

# 绘图
plt.plot(x, y, color='red', linewidth=1.0, linestyle='-')

# 设置坐标轴标签、范围
plt.xlim(0, 2.5)
plt.ylim(0, 2.5)
plt.xlabel('x')
plt.ylabel('y')

# 设置刻度范围及数量
x_ticks = np.linspace(0, 2.5, 10)

plt.xticks(x_ticks)
y_ticks = np.linspace(0, 2.5, 10)
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
ax.set_title('y=sqrt(2*x - x**2)', fontsize=14, color='r')

plt.show()

