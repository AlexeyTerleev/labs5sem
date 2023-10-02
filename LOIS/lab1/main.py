'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Тарбая Данила Игоревич, Терлеев Алексей Сергеевич, Якимович Илья Викторович
Вариант 21:
Реализовать прямой нечеткий логический вывод используя импликацию Геделя
'''

from prettytable import PrettyTable
from src import operations
from src.data_loader import load_from_file

def t_norm(v1, v2):
    return min(v1, v2)

def tmp(set, relation):
    tmp = {}
    for i in relation:
        l = {}
        for j in relation[i]:
            v_set = set[i]
            v_impl = relation[i][j]
            l[j] = t_norm(v_set, v_impl)
        tmp[i] = l
    return tmp

def compress(set):
    conl_set = {}
    row_keys = list(set.keys())
    col_keys = list(set[row_keys[0]].keys())
    for col_key in col_keys:
        conl_set[col_key] = max([set[row_key][col_key] for row_key in row_keys])
    return conl_set


def print_table(name, table):
    x = PrettyTable()
    rows_names = list(table.keys())
    cols_names = [name] + list(table[rows_names[0]].keys())
    x.field_names = cols_names
    for row_name in rows_names:
        x.add_row([row_name, *table[row_name].values()])
    print(x)


def main():
    facts, functions, aims = load_from_file("data")

    function_tables = {}
    for function_head, function_tail in functions.items():
        first_set_name, second_set_name = function_tail
        first_set, second_set = facts[first_set_name], facts[second_set_name]
        function_tables[function_head] = operations.compute_impl(first_set, second_set)

    for table_head, table_tail in function_tables.items():
        print_table(table_head, table_tail)

    result = []
    for aim in aims:
        test = tmp(facts[aim[0]], function_tables[aim[1]])
        print_table(f"{aim[1]}/~\{aim[0]}", test)
        result.append(compress(test))
    
    result_str = [", ".join(f"({pair[0]}, {pair[1]})" for pair in conclusion_set.items()) for conclusion_set in result]
    print("Ответ: {", "}, {".join(result_str), "}.", sep ="")


if __name__ == "__main__":
    main()