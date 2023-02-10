
class Room:
    """
    Класс описывает параметры комнаты
    Примеры:
    >>> room = Room(3, 4, 5)
    """
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        # check length
        if not isinstance(value, (int, float)):
            raise TypeError("Not int or float")
        if not value > 0:
            raise ValueError("Not positive")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        # check width
        if not isinstance(value, (int, float)):
            raise TypeError("Not int or float")
        if not value > 0:
            raise ValueError("Not positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        # check width
        if not isinstance(value, (int, float)):
            raise TypeError("Not int or float")
        if not value > 0:
            raise ValueError("Not positive")
        self._height = value

    @staticmethod
    def area(l, w):
        """
        Метод расчитывает площадь комнаты
        :return: площадь комнаты, м2
        """
        a = l*w
        return a

    @staticmethod
    def volume(l, w, h):
        """
        Метод расчитывает объем комнаты
        :return: объем комнаты, м3
        """
        v = l * w * h
        return v

class Living_room(Room):
    def __init__(self, length: float, width: float, height: float,
                 windows_amount: int, floor_type: str):
        super().__init__(length, width, height)
        self.windows_amount = windows_amount
        self.floor_type = floor_type

    def is_bright(self):
        if self.windows_amount > 2:
            return True
        else:
            return False

    @property
    def floor_type(self):
        return self._floor_type
    @floor_type.setter
    def floor_type(self, value):
        if not isinstance(value, str):
            raise TypeError("Покрытие поля должно быть str")
        self._floor_type = value


if __name__ == "__main__":
    # Write your solution here
    pass
