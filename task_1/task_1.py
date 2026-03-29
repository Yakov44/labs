import json

FILENAME = 'input.json'



def task() -> float:
    with open(FILENAME, 'r', encoding='utf8') as f:
        json_data = json.load(f)

    return round(sum(item['score'] * item['weight'] for item in json_data), 3)



if __name__ == '__main__':
    print(task())

