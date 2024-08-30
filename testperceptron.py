import simpleperceptron as sp
import numpy
from training import dataset
import matplotlib.pyplot as plt 


def main():
    points = dataset()
    neuron1 = sp.Perceptron()
    print(neuron1)
    for pt in points:
        point = [pt.x, pt.y]
        guess = neuron1.train(point, pt.label)
        initPtPlot(pt, guess)
        
    plt.show()
    finalPlot(points)
    plt.show()
    print(neuron1)

def initPtPlot(point, guess):
    if point.label == guess:
        plt.plot(point.x, point.y, marker = 'o', mec = 'k', mfc = 'g')
    else:
        plt.plot(point.x, point.y, marker = 'o', mec = 'k', mfc = 'r')

def finalPlot(points):
    for pt in points:
        plt.plot(pt.x, pt.y, marker = 'o', mec = 'k', mfc = 'g')

if __name__ == '__main__':
    main()
