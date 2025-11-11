# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf8') as f:
        csv_file = csv.DictReader(f)
        csv_file = list(csv_file)
    with open(OUTPUT_FILENAME, 'w', encoding='utf8') as f:
        return json.dump(csv_file, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
