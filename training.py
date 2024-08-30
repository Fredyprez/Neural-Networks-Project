import numpy.random as r
import matplotlib.pyplot as plt 

class Point:
    def __init__(self):
        self.x = r.uniform(0, 500, 1)
        self.y = r.uniform(0,500, 1)
        if self.y  > self.x:
            self.label = 1
        else: self.label = -1
    def __str__(self):
        return f"({self.x}, {self.y})\nlabel: {self.label}"

def dataset():
    points = []
    for i in range(0,500):
        points.append(Point())
    for i in points:
        if i.label == 1:
            plt.plot(i.x, i.y, marker = 'o', mec = 'k', mfc = 'w')
        else:
            plt.plot(i.x, i.y, marker = 'o', mec = 'k', mfc = 'k')
    # x = [0,500]
    # y = [0,500]
    # plt.plot(x,y)
    plt.show()
    return points