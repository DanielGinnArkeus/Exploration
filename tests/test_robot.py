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
        robot.move(Movement(0,1))
        self.assertEqual(robot.location, Location(1,1))
        robot.move(Movement(1,1))
        self.assertEqual(robot.location, Location(2,2))

    def test_movement_success_check(self):
        robot = Robot(Location(0,0))
        result = robot.move(Movement(1,0))
        self.assertTrue(result)
