import dataset as ds
import numpy as np


def selectFlowers(dataset):
    setosas = []
    versicolors = []
    virginicas = []

    for data in dataset:
        if data[-1] is "setosa":
            setosas.append([data[0], data[1], data[2], data[3]])
        elif data[-1] is "versicolor":
            versicolors.append([data[0], data[1], data[2], data[3]])
        elif data[-1] is "virginica":
            virginicas.append([data[0], data[1], data[2], data[3]])
    
    setosas = np.array(setosas)
    versicolors = np.array(versicolors)
    virginicas = np.array(virginicas)

    return setosas, versicolors, virginicas


# use np array please
def dmc(dataset, flowerDimension):
    setosas, versicolors, virginicas = selectFlowers(dataset)

    setosasAverage = reduce(lambda a,b: a+b , setosas, np.array([0,0,0,0])) / len(setosas)
    versicolorsAverage = reduce(lambda a,b: a+b , versicolors, np.array([0,0,0,0])) / len(versicolors)
    virginicasAverage = reduce(lambda a,b: a+b , virginicas, np.array([0,0,0,0])) / len(virginicas)

    flowers = ["setosa", "versicolor", "virginica"]  
    distances = [ 
        ds.euclidianDistanceBetween(flowerDimension, setosasAverage),
        ds.euclidianDistanceBetween(flowerDimension, versicolorsAverage),
        ds.euclidianDistanceBetween(flowerDimension, versicolorsAverage)
    ]

    return flowers[ distances.index(min(distances)) ]


newFlowerDimension = np.array( [ 5.4,  3. ,  4.5,  1.5 ] )
dmc = dmc(ds.irisFlowersDataset, newFlowerDimension)
print(dmc)