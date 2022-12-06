import os
import json

output_dir = 'output/numbers/'
os.makedirs(output_dir, exist_ok=True)


def generate_keys():
    keys = [chr(x) for x in range(33, 127)]
    keys.append('万')  # CHS, JPN
    keys.append('萬')
    keys.append('만')
    keys.append('亿')
    keys.append('億')  # CHT, JPN
    keys.append('억')

    with open(output_dir + 'keys.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(keys))


def generate_stages():
    with open('ArknightsGameData/zh_CN/gamedata/excel/stage_table.json', 'r', encoding="utf-8") as f:
        stages_json = json.loads(f.read())['stages']

    all_stages_code = set()
    for _, v in stages_json.items():
        code = v['code']
        cn_code = False
        for k in code:
            if ord(k) > 127:
                cn_code = True
                break
        if not cn_code:
            all_stages_code.add(code)

    with open(output_dir + 'stages.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(all_stages_code))


def generate_numbers():
    numbers = [str(x) for x in range(1, 10000)]
    for i in range(1, 10000):
        for unit in ['万',  '萬',  '만']:
            numbers.append(str(i) + unit)
            for d in range(1, 10):
                numbers.append(str(i) + '.' + str(d) + unit)

    for i in range(1, 100):
        for unit in ['亿', '億', '억']:
            numbers.append(str(i) + unit)
            for d in range(1, 10):
                numbers.append(str(i) + '.' + str(d) + unit)

    for i in range(1, 1000):
        for unit in ['K', 'M']:
            numbers.append(str(i) + unit)
            for d in range(1, 10):
                numbers.append(str(i) + '.' + str(d) + unit)

    with open(output_dir + 'numbers.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(numbers))


def generate_other():
    # For Public Recruitment
    numbers = ['0' + str(x) for x in range(10)]
    numbers += [str(x) for x in range(10, 60)]

    # All Chars
    numbers += [chr(x) for x in range(33, 127)]

    with open(output_dir + 'other.txt', 'w', encoding="utf-8") as f:
        f.write('\n'.join(numbers))


generate_keys()
generate_stages()
generate_numbers()
generate_other()