import re

class InvalidFactExeption(Exception):
    ...

class InvalidFunctionExeption(Exception):
    ...

class InvalidAimExeption(Exception):
    ...


def fact_is_valid(fact) -> bool:
    
    # p(x)={(a,0),(b,0.3),(c,1)}

    pattern = re.compile(r"^[a-z]\([a-z]\)=\{((\([a-z],\d\.?\d?\),)*(\([a-z],\d\.?\d?\)))?\}$")
    return bool(pattern.match(fact))

def function_is_valid(function) -> bool:
    return True

def aim_is_valid(aim) -> bool:
    return True

