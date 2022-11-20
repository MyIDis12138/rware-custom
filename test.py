import numpy as np
from rware.utils.utils import transform_Pwalls
import random

NUM = 5
size =(7,8)
walls=  [(int(random.random()*NUM),int(random.random()*NUM)) for _ in range(NUM)]
walls_2 = [(0,0),(0,6),(1,4),(2,4),(3,4),(6,0),(6,6)]
test_round = 1
for i in range(test_round):
    p = transform_Pwalls(walls_2, size)
    agent_locs = np.random.choice(
                np.arange(size[0]*size[1]),
                size=5,
                replace=False,
                p=p
            )
    print(agent_locs)
print(0)