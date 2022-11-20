import numpy as np
from typing import List, Tuple

def transform_Pwalls(grid_walls:List[Tuple[int, int]], grid_size):
    len_grid_size = grid_size[0]*grid_size[1]
    walls_yx = np.array([[x[0] for x in grid_walls], [x[1] for x in grid_walls]])
    walls_index = np.ravel_multi_index(walls_yx, grid_size)
    P_walls = np.zeros(len_grid_size,dtype=np.float64)
    uniform_p = 1/(len_grid_size-len(grid_walls))
    for i in range(len_grid_size):
        if not i in walls_index:
            P_walls[i]  = uniform_p
    return P_walls

