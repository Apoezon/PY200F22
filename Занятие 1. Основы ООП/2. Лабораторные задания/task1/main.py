import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Room:
    """
    Класс описывает параметры комнаты
    Примеры:
    >>> room = Room(3, 4, 5)
    """
    def __init__(self, length: float, width: float, height: float):
        # check length
        if not isinstance(length, (int, float)):
            raise TypeError("Not int or float")
        if length < 0:
            raise ValueError("Not positive")
        self.length = float(length)

        # check width
        if not isinstance(width, (int, float)):
            raise TypeError("Not int or float")
        if width < 0:
            raise ValueError("Not positive")
        self.width = width

        # check height
        if not isinstance(height, (int, float)):
            raise TypeError("Not int or float")
        if height < 0:
            raise ValueError("Not positive")
        self.height = height

    def area(self):
        """
        Метод расчитывает площадь комнаты
        :return: площадь комнаты, м2
        """
        a = ...
        return a

    def volume(self):
        """
        Метод расчитывает объем комнаты
        :return: объем комнаты, м3
        """
        v = ...
        return v

class Car:
    """
    Описывает запрос по поиску автомобиля
    Примеры:
    >>> car = Car("Skoda", "Rapid", 2015)  # инициализация экземпляра класса

    """
    def __init__(self, brand: str, model: str, year: int):
        # check brand
        if not isinstance(brand, str):
            raise TypeError("Please enter correct brand name")
        self.brand = brand
        # check model
        if not isinstance(model, str):
            raise TypeError("Please enter correct model name")
        self.model = model
        #check year
        if not isinstance(year, int):
            raise TypeError("Please enter correct production year")
        self.year = year

    def check_price_range(self):
        """
        Возвращает ценовой диапазон предложений
        :return: предложения с max и min ценой
        """
        price_range = ...
        return price_range

    def find_offer(self, distance):
        """
        Возвращает предложения доступные в пределах distance км от меня
        :param distance: расстояние в км
        :return: лист предложений
        """
        offers = ...
        return offers

class Machine:
    def __init__(self, modality: str, model_number: int, serial_number: int):
        """
        Опсывает параметры объекта Machine
        :param modality: тип устройства
        :param model_number: модель устройства
        :param serial_number: серийный номер

        Примеры:
        >>> xp = Machine("XP",832994, 1243)  # инициализация экземпляра класса
        """
        modality_list = ('US', 'XP', 'CT', 'AX', 'MR', 'RO')
        # check modality
        if not isinstance(modality, str):
            raise TypeError('Modality should be two capital letters')
        if modality not in modality_list:
            raise ValueError('Mo such modality exists')
        self.modality = modality
        # check model number
        if not isinstance(model_number, int):
            raise TypeError("Model number is interger number starting from 1")
        if model_number < 0:
            model_number = abs(model_number)
        self.model_number = model_number
        # check serial number
        if not isinstance(serial_number, int):
            raise TypeError("Serial number is interger number starting from 1")
        if serial_number < 0:
            serial_number = abs(serial_number)
        self.serial_number = serial_number

    def check_EOS(self) -> bool:
        """
        Проверяет модель на EOS (конец поддержки)
        :return: Модель больше не поддерживается
        """
        discontinued = ...
        return discontinued

    def check_contract(self) -> list:
        """
        Возвращает пункты контракты, необходимые для сервиса
        :return: условия обслуживания по контракту
        """
        contract_terms = ...
        return contract_terms


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    room = Room(3.1, 4, 7.3)
    car = Car("Mazda", "6", 2017)
    us = Machine("US", 123456, 4321)
    print(doctest.testmod())
