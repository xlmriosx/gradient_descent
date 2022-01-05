from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

# function
def f(x,y):
  return x**2 + y**2;

# Graph function
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

res = 100

X = np.linspace(-4, 4, res)
Y = np.linspace(-4, 4, res)

X, Y = np.meshgrid(X, Y)

Z = f(X,Y)


surf = ax.plot_surface(X, Y, Z, cmap=cm.cool,
                       linewidth=0, antialiased=False)

fig.colorbar(surf)
plt.title('Function')
plt.show()

# Graph surface or heat map
level_map = np.linspace(np.min(Z), np.max(Z),res)
plt.contourf(X, Y, Z, levels=level_map,cmap=cm.cool)
plt.colorbar()
plt.title('Gradient Descent')


# Calcuate gradient descent
def derivate(_p,p):
  return  (f(_p[0],_p[1]) - f(p[0],p[1])) / h

p = np.random.rand(2) * 8 - 4 # generate two randon values

plt.plot(p[0],p[1],'o', c='k')

lr = 0.01
h = 0.01

grad = np.zeros(2)

for i in range(10000):
  for idx, val in enumerate(p):
    _p = np.copy(p)

    _p[idx] = _p[idx] + h;

    dp = derivate(_p,p)

    grad[idx] = dp

  p = p - lr * grad

  if(i % 10 == 0):
    plt.plot(p[0],p[1],'o', c='r')

plt.plot(p[0],p[1],'o', c='w')
plt.text(s=f"The minimun point in: {p}", x=-3, y=3)
plt.show()



