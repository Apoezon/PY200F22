import unittest
from main import *  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    def test_init(self):
        room = Room(1, 2, 3)
        self.assertEqual(room.length, 1)
        self.assertEqual(room.width, 2)
        self.assertEqual(room.height, 3)
        # Следующее, наверно, написано больше для % в coverage
        self.assertEqual(room._length, 1)
        self.assertEqual(room._width, 2)
        self.assertEqual(room._height, 3)

    def test_init_value(self):

        for i in [-1, 0]:
            with self.assertRaises(ValueError):
                room = Room(i, 2, 3)
                room = Room(1, i, 3)
                room = Room(1, 2, i)

    def test_init_type(self):

        for j in [None, (1, 2), [3, 4], ""]:
            with self.assertRaises(TypeError):
                room = Room(j, 2, 3)
                room = Room(1, j, 3)
                room = Room(1, 2, j)

    def test_area(self):
        self.assertEqual(Room.area(2,3), 6)

    def test_volume(self):
        self.assertEqual(Room.volume(2, 3, 4), 24)

    def test_floor_type(self):
        with self.assertRaises(TypeError):
            liv_room = Living_room(4, 5, 3, 3, 5)

    def test_living_room(self):
        liv_room = Living_room(4, 5, 3, 3, "wood")
        self.assertEqual(liv_room.length, 4)
        self.assertEqual(liv_room.width, 5)
        self.assertEqual(liv_room.height, 3)
        self.assertEqual(liv_room.windows_amount, 3)
        self.assertEqual(liv_room.floor_type, "wood")
        # Следующее, наверно, написано больше для % в coverage
        self.assertEqual(liv_room._length, 4)
        self.assertEqual(liv_room._width, 5)
        self.assertEqual(liv_room._height, 3)
        self.assertEqual(liv_room._floor_type, "wood")


if __name__ == '__main__':
    unittest.main()
