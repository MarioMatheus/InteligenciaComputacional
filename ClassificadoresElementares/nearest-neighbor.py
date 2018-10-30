# import numpy as np
import dataset as ds

def nearestNeighbor(dataset, flowerDimension):
    distances = list(
        map(lambda flowerPoint: ds.euclidianDistanceBetween(flowerPoint, flowerDimension), dataset)
    )
    minimunDistanceIndex = distances.index(min(distances))
    return(dataset[minimunDistanceIndex][-1])

    

newFlowerDimension = [ 5.4,  3. ,  4.5,  1.5 ]
nn = nearestNeighbor(ds.irisFlowersDataset, newFlowerDimension)
print(nn)
