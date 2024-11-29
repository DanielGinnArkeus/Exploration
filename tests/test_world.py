from unittest import TestCase
import numpy as np
from src.world.map import World


class TestWorld(TestCase):
    def test_world_init(self):
        map_size = (3,3)
        map = World(map_size)
        self.assertEqual(map.map.shape, map_size)

    def test_world_border(self):
        map_size = (3,3)
        map = World(map_size)
        test_map = np.ones(map_size)
        test_map[1,1] = 0
        np.testing.assert_equal(map.map, test_map)

