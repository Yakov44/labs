"""
Модуль фермера.
Содержит класс Farmer для управления фермером и его работой.
"""

from potato_bed import PotatoBed


class Farmer:
    """Фермер с инвентарем и методами работы.

    >>> farmer = Farmer("Иван", 35)
    >>> farmer.name
    'Иван'
    >>> farmer.age
    35
    >>> farmer.inventory
    []

    >>> farmer.get_info()
    'Фермер Иван, возраст: 35'
    """

    def __init__(self, name, age):
        """Создает фермера с указанным именем и возрастом.

        >>> f = Farmer("Мария", 28)
        >>> f.name
        'Мария'
        >>> f.age
        28
        >>> f.inventory
        []
        """
        self.name = name
        self.age = age
        self.inventory = []  # Изначально пустой инвентарь

    def get_info(self):
        """Возвращает информацию о фермере.

        >>> farmer = Farmer("Петр", 40)
        >>> farmer.get_info()
        'Фермер Петр, возраст: 40'

        >>> farmer2 = Farmer("Анна", 25)
        >>> farmer2.get_info()
        'Фермер Анна, возраст: 25'
        """
        return f"Фермер {self.name}, возраст: {self.age}"

    def work(self, bed):
        """Фермер работает на грядке: поливает и собирает урожай.

        >>> farmer = Farmer("Иван", 35)
        >>> bed = PotatoBed(3, 4)  # Почти созревшая картошка

        >>> farmer.work(bed)  # Работаем один раз
        >>> farmer.inventory
        []

        >>> farmer.work(bed)  # Работаем второй раз
        >>> len(farmer.inventory)
        3
        >>> len(bed)
        0

        >>> bed2 = PotatoBed(2, 0)
        >>> for _ in range(6):  # 6 раз работаем на новой грядке
        ...     farmer.work(bed2)
        >>> len(farmer.inventory)
        5
        """
        # Поливаем картошку (увеличиваем стадию)
        bed.grow_all()

        # Пытаемся собрать урожай, если картошка созрела
        try:
            harvested = bed.harvest()
            self.inventory.extend(harvested)
            print(f"{self.name} собрал урожай: {len(harvested)} картошек!")
        except ValueError:
            print(f"{self.name} полил грядку. Картошка еще не созрела.")

    def show_inventory(self):
        """Показывает содержимое инвентаря.

        >>> farmer = Farmer("Тест", 30)
        >>> farmer.show_inventory()
        Инвентарь пуст

        >>> bed = PotatoBed(2, 5)
        >>> farmer.work(bed)
        >>> farmer.show_inventory()
        В инвентаре 2 картошек
        """
        if not self.inventory:
            print("Инвентарь пуст")
        else:
            print(f"В инвентаре {len(self.inventory)} картошек")

    def __repr__(self):
        return f"Фермер({self.name}, {self.age} лет)"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)