from itertools import permutations
from random import shuffle
from typing import Iterable


def read_employees() -> list[str]:
    """"Собираем список все сотрудников"""
    with open('employees.csv', 'r') as file:
        return [i.replace('\n', '') for i in file]


def read_pairs() -> list[list[str]]:
    """Собираем все пары сотрудников, которые уже встречались"""
    with open('pairs.csv', 'r') as file:
        return [i.replace('\n', '').split(', ') for i in file]


def write_pairs(pair_list: list[list[str]]) -> None:
    """Записываем пары, которые нам выпали, в участвовавшие"""
    with open('pairs.csv', 'a') as file:
        for i in pair_list:
            file.write(f'{i[0]}, {i[1]}\n')
            file.write(f'{i[1]}, {i[0]}\n')


def write_result(pair_list: list[list[str]]) -> None:
    """Выводим список пар, которые еще не участвовали"""
    with open('result.csv', 'w') as file:
        for i in pair_list:
            file.write(f'{i[0]}, {i[1]}\n')


def check_odd_list(check_list: list) -> list[str]:
    """Если количество сотрудников нечетное - добавляем id=0"""
    return check_list if len(check_list) % 2 == 0 else check_list+['0']


def generate_combinations(employees: list[str]) -> Iterable[str]:
    """Формируем генератор всех возможных вариантов пар"""
    shuffle(employees)
    return permutations(employees)


def check_pairs(pair_list: Iterable[str], finished_pairs: list[list[str]]) -> list[list[str]]:
    """Если в варианте из генератора нет участвовавших пар - выводим"""
    for line in pair_list:
        line_list = list(line)
        result: list[list[str]] = [line_list[i:i + 2] for i in range(0, len(line_list), 2)]
        if not any(i in result for i in finished_pairs):
            return result


if __name__ == '__main__':
    employee_list: list[str] = check_odd_list(read_employees())
    participating_pairs: list[list[str]] = read_pairs()
    pair_generator: Iterable[str] = generate_combinations(employee_list)
    final_pairs: list[list[str]] = check_pairs(pair_generator, participating_pairs)
    write_result(final_pairs)
    write_pairs(final_pairs)
