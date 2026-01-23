"""
Модуль картошки.
Содержит класс Potato, представляющий картошку с определенной стадией зрелости.
"""


class Potato:
    """Картошка с определенной стадией зрелости.

    >>> potato = Potato(0)
    >>> potato.stage
    0
    >>> potato.is_ripe()
    False

    >>> potato.grow()
    >>> potato.stage
    1
    >>> potato.grow()
    >>> potato.is_ripe()
    True

    >>> potato2 = Potato(5)
    >>> potato2.stage
    5
    >>> potato2.is_ripe()
    True
    """

    def __init__(self, stage=0):
        """Создание картошки с начальной стадией зрелости.

        >>> p = Potato()
        >>> p.stage
        0

        >>> p2 = Potato(3)
        >>> p2.stage
        3
        """
        self.stage = stage  # 0-4 - растет, 5 - созрела

    def grow(self):
        """Увеличивает стадию зрелости картошки на 1.

        >>> p = Potato(0)
        >>> p.grow()
        >>> p.stage
        1

        >>> p2 = Potato(5)
        >>> p2.grow()
        >>> p2.stage
        6
        """
        self.stage += 1

    def is_ripe(self):
        """Проверяет, созрела ли картошка.

        >>> p = Potato(0)
        >>> p.is_ripe()
        False

        >>> p2 = Potato(5)
        >>> p2.is_ripe()
        True

        >>> p3 = Potato(4)
        >>> p3.is_ripe()
        False
        """
        return self.stage >= 5

    def __repr__(self):
        return f"Картошка(стадия: {self.stage})"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)