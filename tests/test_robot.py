from unittest import TestCase
from src.robots.robot import Robot
from src.robots.robot import Location, Movement


class TestRobot(TestCase):
    def test_init(self):
        robot = Robot(Location(0,0))
        self.assertEqual(robot.location, Location(0,0))

    def test_simple_move(self):
        robot = Robot(Location(0,0))
        robot.move(Movement(1,0))
        self.assertEqual(robot.location, Location(1,0))
