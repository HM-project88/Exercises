
# For solving the error we have to replace "import numpy as np" to the first part of program
import numpy as np
# For fixing the wrong I used an auxiliary variable and the problem solved
auxiliary=np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])
def swap(coords: np.ndarray):
    #coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
    auxiliary[:,0]=coords[:,1]
    auxiliary[:, 1] = coords[:, 1]
    auxiliary[:, 2] = coords[:, 3]
    auxiliary[:, 3] = coords[:, 2]
    auxiliary[:, 4] = coords[:, 4]
    coords=auxiliary
    return coords

coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])
swapped_coords = swap(coords)
print(swapped_coords)