import re

class InvalidFunctionExeption(Exception):
    def __init__(self, func: str) -> None:
        super().__init__(f"Invalid format of function: {func}")

class InvalidAimExeption(Exception):
    def __init__(self, aim: str) -> None:
        super().__init__(f"Invalid format of aim: {aim}")


class Fact:

    class InvalidFactExeption(Exception):
        def __init__(self, fact: str) -> None:
            super().__init__(f"Invalid format of fact: {fact}")

    def __init__(self, fact: str) -> None:
        self.fact = fact
        if not self.__is_valid():
            raise Fact.InvalidFactExeption(fact)
        self.head = self.__get_head()
        self.tail = self.__get_tail()
        if not self.__tail_is_valid():
            raise Fact.InvalidFactExeption(fact)

    def __is_valid(self):
        # p(x)={(a,0),(b,0.3),(c,1)}
        pattern = re.compile(r"^[a-z]\([a-z]\)={(\([a-z],\d(\.\d)?\),)*(\([a-z],\d(\.\d)?\))?}$")
        return bool(pattern.match(self.fact))
    
    def __get_head(self):
        head_tail_pattern = r"^(.+)={(.*)}$"
        return re.match(head_tail_pattern, self.fact).group(1)

    def __get_tail(self):
        head_tail_pattern = r"^(.+)={(.*)}$"
        pairs_str = re.match(head_tail_pattern, self.fact).group(2)
        pairs = [tuple(pair.split(",")) for pair in pairs_str[1:-1].split("),(")]
        if len(pairs[0]) == 1:
            return None
        else:
            return tuple(map(lambda x: (x[0], float(x[1])), pairs))  
    
    def __tail_is_valid(self):
        if self.tail is None:
            return True
        else:
            return len(set(map(lambda x: x[0], self.tail))) == len(list(map(lambda x: x[0], self.tail)))

    
def function_is_valid(function) -> bool:
    return True

def aim_is_valid(aim) -> bool:
    return True

