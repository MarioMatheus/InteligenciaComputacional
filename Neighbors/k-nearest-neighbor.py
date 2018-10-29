import dataset as ds
import numpy as np
import operator

def selectFlowers(setosas, versicolors, virginicas, dataset):
    for data in dataset:
        if data[-1] is "setosa":
            setosas.append([data[0], data[1], data[2], data[3]])
        elif data[-1] is "versicolor":
            versicolors.append([data[0], data[1], data[2], data[3]])
        else:
            virginicas.append([data[0], data[1], data[2], data[3]])
    setosas = np.array(setosas)
    versicolors = np.array(versicolors)
    virginicas = np.array(virginicas)

def kNearestNeighbor(dataset, flowerDimension):
    setosas = []
    versicolors = []
    virginicas = []

    selectFlowers(setosas, versicolors, virginicas, dataset)
    print(reduce(lambda a,b: a + b, setosas))
    # print(setosas[0])

kNearestNeighbor(ds.irisFlowersDataset, None)