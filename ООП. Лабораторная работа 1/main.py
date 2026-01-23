"""
Главный модуль для демонстрации работы всех классов.
"""

from farmer import Farmer
from potato_bed import PotatoBed


def main():
    """Основная функция для демонстрации работы фермера."""

    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФЕРМЕРА")
    print("=" * 50)

    # Создаем фермера
    farmer = Farmer("Василий", 42)
    print(f"Создан фермер: {farmer.get_info()}")

    # Создаем грядку с картошкой
    bed = PotatoBed(5, 3)  # 5 картошек на 3 стадии
    print(f"\nСоздана грядка с {len(bed)} картошками")
    print(f"Состояние грядки: {bed}")

    # Фермер работает на грядке несколько дней
    print("\n" + "=" * 50)
    print("НАЧАЛО РАБОТЫ НА ГРЯДКЕ")
    print("=" * 50)

    days_to_work = 5
    for day in range(1, days_to_work + 1):
        print(f"\n{'=' * 20} День {day} {'=' * 20}")
        print(f"До работы: {bed}")

        farmer.work(bed)
        farmer.show_inventory()

        print(f"После работы: {bed}")

    # Итоги
    print("\n" + "=" * 50)
    print("ИТОГИ РАБОТЫ")
    print("=" * 50)
    print(farmer.get_info())
    print(f"Всего собрано картошек: {len(farmer.inventory)}")

    # Дополнительная демонстрация
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНАЯ ДЕМОНСТРАЦИЯ")
    print("=" * 50)

    # Создаем нового фермера и грядку
    farmer2 = Farmer("Мария", 28)
    bed2 = PotatoBed(3, 0)

    print(f"\nНовый фермер: {farmer2.get_info()}")
    print(f"Новая грядка: {bed2}")

    # Работаем до полного сбора урожая
    work_count = 0
    while len(bed2) > 0:
        work_count += 1
        print(f"\nРабота #{work_count}:")
        farmer2.work(bed2)

    print(f"\n{farmer2.name} собрала весь урожай за {work_count} дней!")
    farmer2.show_inventory()


def run_tests():
    """Запускает все доктесты из модулей."""
    import doctest

    print("=" * 50)
    print("ЗАПУСК ДОКТЕСТОВ")
    print("=" * 50)

    # Импортируем модули для тестирования
    import potato
    import potato_bed
    import farmer

    # Запускаем тесты для каждого модуля
    print("\n1. Тестирование модуля potato.py:")
    result_potato = doctest.testmod(potato, verbose=False)
    print(f"   Пройдено: {result_potato.attempted - result_potato.failed}/{result_potato.attempted}")

    print("\n2. Тестирование модуля potato_bed.py:")
    result_bed = doctest.testmod(potato_bed, verbose=False)
    print(f"   Пройдено: {result_bed.attempted - result_bed.failed}/{result_bed.attempted}")

    print("\n3. Тестирование модуля farmer.py:")
    result_farmer = doctest.testmod(farmer, verbose=False)
    print(f"   Пройдено: {result_farmer.attempted - result_farmer.failed}/{result_farmer.attempted}")

    if result_potato.failed == 0 and result_bed.failed == 0 and result_farmer.failed == 0:
        print("\n✓ Все тесты пройдены успешно!")
    else:
        print("\n⚠ Некоторые тесты не пройдены")

    return result_potato.failed + result_bed.failed + result_farmer.failed


if __name__ == "__main__":
    # Выбираем режим работы
    print("Выберите режим работы:")
    print("1 - Демонстрация работы фермера")
    print("2 - Запуск доктестов")
    print("3 - И то, и другое")

    try:
        choice = int(input("Введите номер (1-3): ").strip())
    except ValueError:
        choice = 3

    print("\n")

    if choice == 1:
        main()
    elif choice == 2:
        run_tests()
    else:
        run_tests()
        print("\n" + "=" * 50)
        main()