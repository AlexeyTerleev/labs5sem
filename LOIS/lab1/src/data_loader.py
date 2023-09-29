from typing import List, Dict, Tuple

from .data_validators import *


def load_from_file(path):
    facts, functions, aims = None, None, None
    with open(path, "r") as file:
        facts, functions, aims = (tuple("".join(x.split()) for x in line.split("\n")) for line in file.read().split("\n\n"))
    for fact in facts:
        if not fact_is_valid(fact):
            raise InvalidFactExeption    
    for function in functions:
        if not function_is_valid(function):
            raise InvalidFunctionExeption
    for aim in aims:
        if not aim_is_valid(aim):
            raise InvalidAimExeption
    return get_facts_dict(facts), get_functions_dict(functions), aims


def get_facts_dict(facts_list: List[str]):# -> Dict[str: Dict[str: float]]:
    facts_dct = {}
    for fact in facts_list:
        facts_dct[get_fact_name(fact)] = get_fact_logic(fact)
    return facts_dct


def get_fact_name(fact: str) -> str:
    return fact.split("=")[0]


def get_fact_logic(fact: str): # -> Dict[str: float]:
    logic = fact.split("=")[1]
    logic_pairs = {get_logic_pair(pair)[0]: get_logic_pair(pair)[1] for pair in get_logic_pairs_sep_by_comma(logic)}
    return logic_pairs


def get_logic_pairs_sep_by_comma(logic: str) -> List[str]:
    return logic[2:-2].split("),(")


def get_logic_pair(logic_pair_sep_by_comma: str) -> Tuple[str, float]:
    name, value =  logic_pair_sep_by_comma.split(",")
    return name, float(value)


def get_functions_dict(functions: List[str]): # -> Dict[str: str]:
    functions_dct = {}
    for function in functions:
        name, logic = function.split("=")
        functions_dct[name] = logic
    return functions_dct

    
