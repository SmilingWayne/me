import numpy as np
import matplotlib.pyplot as plt

w = np.array([500, 300, 700, 225, 150, 250,175, 300])
h = np.array([0.9, 0.95, 0.85, 1.50, 1.50, 1.50, 1.50, 1.50])
p = np.array([[700, 1200],[250, 600],[225, 825], [600, 500],\
[1050, 1200],[800, 300], [925, 975], [1000, 1080]])

Wc = np.array(w) * np.array(h)
Wcx = (p[:,0] * Wc).sum()
Wcy = (p[:,1] * Wc).sum()
x0 = Wcx / Wc.sum()
y0 = Wcy / Wc.sum()
d_j = ((p[:,0] - x0)**2 + (p[:,1]-y0)**2)**0.5
T = (Wc * d_j).sum()

print('迭代前总费用T0{}'.format(T))
plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.figure(figsize=(10,10))
for i in range(20):
    Wc_j = Wc/d_j
    Wcx_j = ((p[:,0] * Wc)/d_j).sum()
    Wcy_j = ((p[:,1] * Wc)/d_j).sum()
    x = Wcx_j / Wc_j.sum()
    y = Wcy_j / Wc_j.sum()
    d_j = ((p[:,0] - x)**2 + (p-y)[:,1]**2)**0.5
    T = (Wc * d_j).sum()
    print(f"第{i}次后：x = {round(x,1)}, y = {round(y,1)},\
         成本{round(T,1)}")
    print('经{}次迭代后选址点位置：({},{})'.format(i+1,x,y))
    print('总费用T{}：{}'.format(i+1,T))

# ===================================================
plt.figure(figsize=(5,10))
plt.subplot(2,1,1)
plt.scatter(p[:,0],p[:,1],c = 'green',marker = '*',\
    alpha = 0.7,s = 100,label='配送点')
plt.scatter([658.5],[854.0],c = 'red', s = 100,marker = 'p',alpha = 0.7,label='选址点')
plt.grid(True)
plt.title('第1次结果',fontsize=12)
plt.legend(loc='best')

plt.subplot(2,1,2)
plt.scatter(p[:,0],p[:,1],c = 'green',marker = '*',\
    alpha = 0.7,s = 100,label='配送点')
plt.scatter(x,y,c = 'red', s = 100,marker = 'p',alpha = 0.7,label='选址点')
plt.grid(True)
plt.title('第{}次结果'.format(i+1),fontsize=12)
plt.legend(loc='best')

