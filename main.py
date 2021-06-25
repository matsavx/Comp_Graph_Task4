import matplotlib.pyplot as plt
import random

n = 13
V = []
V = range(n)

points = []
x = 0
y = 0

for i in V:
    x = random.randint(0, 20)
    y = random.randint(0, 20)
    points.append((x, y))

points.append(points[0])

xs, ys = zip(*points)
points.clear()

plt.figure()
plt.plot(xs, ys)
plt.show()
