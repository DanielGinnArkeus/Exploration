import numpy as np
from typing import Tuple

class World:
    def __init__(self, size: Tuple[np.uint16,np.uint16]) -> None:
        assert(size[0] >= 3 and size[1] >= 3)
        self.map = np.ones(size, dtype=np.int8)
        self.map[1:-1,1:-1] = np.zeros((size[0]-2, size[1]-2), dtype=np.int8)

