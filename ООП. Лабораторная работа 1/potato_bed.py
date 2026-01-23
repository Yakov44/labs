"""
Модуль грядки с картошкой.
Содержит класс PotatoBed для управления грядкой картошки.
"""

from potato import Potato


class PotatoBed:
    """Грядка с картошкой.

    >>> bed = PotatoBed(3)
    >>> len(bed.potatoes)
    3
    >>> bed.is_all_ripe()
    False

    >>> bed.grow_all()
    >>> bed.potatoes[0].stage
    1

    >>> bed2 = PotatoBed(2, 5)
    >>> bed2.is_all_ripe()
    True
    """

    def __init__(self, count, initial_stage=0):
        """Создает грядку с указанным количеством картошек.

        >>> bed = PotatoBed(5)
        >>> len(bed.potatoes)
        5

        >>> bed2 = PotatoBed(3, 2)
        >>> bed2.potatoes[0].stage
        2
        """
        self.potatoes = [Potato(initial_stage) for _ in range(count)]

    def grow_all(self):
        """Увеличивает стадию зрелости всех картошек на грядке.

        >>> bed = PotatoBed(2, 0)
        >>> bed.grow_all()
        >>> bed.potatoes[0].stage
        1
        >>> bed.potatoes[1].stage
        1

        >>> bed2 = PotatoBed(1, 4)
        >>> bed2.grow_all()
        >>> bed2.potatoes[0].stage
        5
        """
        for potato in self.potatoes:
            potato.grow()

    def is_all_ripe(self):
        """Проверяет, созрели ли все картошки на грядке.

        >>> bed = PotatoBed(2, 0)
        >>> bed.is_all_ripe()
        False

        >>> bed2 = PotatoBed(3, 5)
        >>> bed2.is_all_ripe()
        True

        >>> bed3 = PotatoBed(2, 4)
        >>> bed3.is_all_ripe()
        False
        """
        return all(potato.is_ripe() for potato in self.potatoes)

    def harvest(self):
        """Собирает урожай, если все картошки созрели.

        >>> bed = PotatoBed(2, 5)
        >>> harvested = bed.harvest()
        >>> len(harvested)
        2
        >>> len(bed.potatoes)
        0

        >>> bed2 = PotatoBed(2, 3)
        >>> bed2.harvest()
        Traceback (most recent call last):
            ...
        ValueError: Не все картошки созрели!
        """
        if not self.is_all_ripe():
            raise ValueError("Не все картошки созрели!")

        harvested = self.potatoes.copy()
        self.potatoes = []
        return harvested

    def __len__(self):
        """Возвращает количество картошек на грядке.

        >>> bed = PotatoBed(4)
        >>> len(bed)
        4
        """
        return len(self.potatoes)

    def __repr__(self):
        ripe_count = sum(1 for p in self.potatoes if p.is_ripe())
        return f"Грядка(всего: {len(self)}, созрело: {ripe_count})"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)