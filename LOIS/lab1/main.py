'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Тарбая Данила Игоревич, Терлеев Алексей Сергеевич, Якимович Илья Викторович
Вариант 21:
Реализовать прямой нечеткий логический вывод используя импликацию Геделя
'''

import json 
from src import operations

def t_norm(v1, v2):
    return min(v1, v2)


    
    
def neg(set1):
    return {x: 1 - y for x, y in set1}

def conclusion(set, relation):
    conl_set = {}
    for i in relation:
        l = []
        for j in relation[i]:
            v_set = set[i]
            v_impl = relation[i][j]
            l.append(t_norm(v_set, v_impl))
        value = max(l)
        conl_set[i] = value
    return conl_set

with open("data", "r") as file : 
    lst = []
    for line in file:
        lst.append(json.loads(line))
        
A, B = lst

relation = operations.compute_impl(A, B)

conclusion_set = conclusion(A, relation)

print("B' = {", ", ".join(f"({x[0]}, {x[1]})" for x in conclusion_set.items()), "}", sep="")
test()