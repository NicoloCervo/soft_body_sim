import itertools
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def neighbors(point):
    x, y = point
    for i, j in itertools.product(range(-1, 2), repeat=2):
        if any((i, j)):
            yield (x + i, y + j)

def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))

    for point in recalc:
        count = sum((neigh in board)
                for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)

    return newstate

    
start=[]
for i in range(-15,16):
    for j in range(-15,16):
        if random.randint(0,1):
            start.append((i,j))


glider = set(start)

fig, ax = plt.subplots()

x, y = zip(*glider)
mat, = ax.plot(x, y, '.')

def animate(i):
    global glider
    glider = advance(glider)
    x, y = zip(*glider)
    mat.set_data(x, y)
    return mat,

ax.axis([-100,100,-100,100])
ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()