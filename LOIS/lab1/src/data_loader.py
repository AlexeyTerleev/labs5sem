from typing import List, Dict, Tuple

from .data_validators import *


def load_from_file(path):
    facts, functions, aims = None, None, None
    with open(path, "r") as file:
        facts, functions, aims = (tuple("".join(x.split()) for x in line.split("\n")) for line in file.read().split("\n\n"))
    
    facts = [Fact(fact) for fact in facts]

    for function in functions:
        if not function_is_valid(function):
            raise InvalidFunctionExeption(function)
    for aim in aims:
        if not aim_is_valid(aim):
            raise InvalidAimExeption(aim)
    return get_facts_dict(facts), get_functions_dict(functions), aims


def get_facts_dict(facts_list: List[Fact]):
    return {fact.head: fact.tail for fact in facts_list}


def get_functions_dict(functions: List[str]): # -> Dict[str: str]:
    functions_dct = {}
    for function in functions:
        name, logic = function.split("=")
        functions_dct[name] = logic
    return functions_dct

    
