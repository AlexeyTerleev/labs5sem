from typing import List

from .data_validators import *


def load_from_file(path):
    facts, rules = None, None
    with open(path, "r") as file:
        facts, rules = (tuple("".join(x.split()) for x in line.split("\n")) for line in file.read().split("\n\n"))
    facts = [Fact(fact) for fact in facts]
    rules = [Rule(rule) for rule in rules]
    return get_facts_dict(facts), get_rules_dict(rules)


def get_facts_dict(facts: List[Fact]):
    return {fact.head_without_variables: fact for fact in facts}

def get_rules_dict(rules: List[Rule]):
    return {rule.head_without_variables: rule for rule in rules}


    
