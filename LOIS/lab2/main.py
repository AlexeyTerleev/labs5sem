'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Тарбая Данила Игоревич, Терлеев Алексей Сергеевич, Якимович Илья Викторович
Вариант 21:
Реализовать прямой нечеткий логический вывод используя импликацию Геделя
'''


from src import operations
from src.data_loader import load_from_file, get_facts_dict
from src.data_validators import Fact
from src.utils import print_table

import os


def main(dir: str):


    for i, filename in enumerate(sorted(os.listdir(dir))):
        try:
            if i != 0:
                return
            file = os.path.join(dir, filename)
            if not os.path.isfile(file):
                print(f"Skip {file} (isn't a file)")
                continue

            facts, rules = load_from_file(file)
            print(facts["p()"].tail)
            print(rules["f()"].tail)
        except Exception as e: 
            raise e


if __name__ == "__main__":
    main("data")

# Отчет (проверить нормализованные и субнормализованные множества (пары до и после импликации))
