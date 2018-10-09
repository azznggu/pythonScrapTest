
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.style as style
import random

style.use = "fivethirtyeight"
figure = plt.figure()
ax = figure.add_subplot(1,1,1)

def draw(a) :

    x = []
    y = []

    for i in range(1,10) :
        x.append(i)
        y.append(random.randint(1,10))
    ax.clear()
    ax.plot(x,y)


ani = animation.FuncAnimation(figure,draw,interval=1000)
plt.show()



