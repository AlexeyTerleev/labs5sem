from typing import List, Dict, Tuple

from .data_validators import *


def load_from_file(path):
    facts, functions, aims = None, None, None
    with open(path, "r") as file:
        facts, functions, aims = (tuple("".join(x.split()) for x in line.split("\n")) for line in file.read().split("\n\n"))
    
    facts = [Fact(fact) for fact in facts]
    functions = [Function(function) for function in functions]
    aims = [Aim(aim) for aim in aims]
    return get_facts_dict(facts), get_functions_dict(functions), get_aims_tuple(aims)


def get_facts_dict(facts: List[Fact]):
    return {fact.head: fact.tail for fact in facts}

def get_functions_dict(functions: List[Function]):
    return {func.head: func.tail for func in functions}

def get_aims_tuple(aims: List[Aim]):
    return tuple(aim.pair for aim in aims)

    
