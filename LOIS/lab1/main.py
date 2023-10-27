'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Тарбая Данила Игоревич, Терлеев Алексей Сергеевич, Якимович Илья Викторович
Вариант 21:
Реализовать прямой нечеткий логический вывод используя импликацию Геделя
'''


from src import operations
from src.data_loader import load_from_file
from src.utils import print_table

import os


def main(dir: str):


    for i, filename in enumerate(sorted(os.listdir(dir))):

        print(f"{'-' * 10}{i + 1}{'-' * 10}")
        
        file = os.path.join(dir, filename)
        if not os.path.isfile(file):
            print(f"Skip {file} (isn't a file)")
            continue
        
        print("Input:")
        with open(file, "r") as f:
            print(f.read())
        print()

        print("Solution:")
        facts, functions = load_from_file(file)

        function_tables, function_tables_titles = {}, []
        for function_head, function_obj in functions.items():
            function_tables_titles.append(function_obj.head)
            first_set_name, second_set_name = function_obj.tail_without_variables
            first_set, second_set = facts[first_set_name], facts[second_set_name]
            function_tables[function_head] = operations.matrix_impl(first_set.tail, second_set.tail)

        for table_title, table_tail in zip(function_tables_titles, function_tables.values()):
            print_table(table_title, table_tail)

        result = []

        for table_title, function_table in zip(function_tables_titles, function_tables.values()):
            for fact in facts.values():
                try:
                    tmp = operations.built_impl_table(fact.tail, function_table)
                    print_table(f"{table_title}/~\{fact.head}", tmp)
                    result.append(operations.compress(tmp))
                except ValueError:
                    ...
        
        result_str = [", ".join(f"({pair[0]}, {pair[1]})" for pair in conclusion_set.items()) for conclusion_set in result]
        print()
        
        print("Answear: {", "}, {".join(result_str), "}.", sep ="")
        print()


if __name__ == "__main__":
    main("data")

# Отчет (проверить нормализованные и субнормализованные множества (пары до и после импликации))
