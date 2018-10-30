import dataset as ds
import numpy as np
import operator

def kNearestNeighbor(k, dataset, flowerDimension):
    distances = list(
        map(lambda flowerPoint: ds.euclidianDistanceBetween(flowerPoint, flowerDimension), dataset)
    )
    distancesOrdered = sorted(distances)
    
    flowers = ["setosa", "versicolor", "virginica"]
    numbers = [0, 0, 0]
    for i in range(k):
        flower = dataset[ distances.index(distancesOrdered[i]) ][-1]
        numbers[ flowers.index(flower) ] += 1

    return flowers[ numbers.index(max(numbers)) ]




newFlowerDimension = [ 5.4,  3. ,  4.5,  1.5 ]
knn = kNearestNeighbor(8, ds.irisFlowersDataset, newFlowerDimension)
print(knn)

