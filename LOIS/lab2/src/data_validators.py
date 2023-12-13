import re

def remove_variables(head: str):
    name = head.split("(")[0]
    num_of_comma = head.count(",")
    return f"{name}({',' * num_of_comma})"

class Fact:

    class InvalidFactExeption(Exception):
        def __init__(self, fact: str) -> None:
            super().__init__(f"Invalid format of fact: {fact}")

    def __init__(self, fact: str, valid_check=True) -> None:
        self.fact = fact
        if valid_check and not self.__is_valid():
            raise Fact.InvalidFactExeption(fact)
        self.head = self.__get_head()
        self.head_without_variables = remove_variables(self.head)
        self.tail = self.__get_tail()
        if not self.__tail_is_valid():
            raise Fact.InvalidFactExeption(fact)
        self.tail = {pair[0]: pair[1] for pair in self.tail}

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
        return tuple() if len(pairs[0]) == 1 else tuple(map(lambda x: (x[0], float(x[1])), pairs))  
    
    def __tail_is_valid(self):
        return len(set(map(lambda x: x[0], self.tail))) == len(list(map(lambda x: x[0], self.tail)))


class Rule:

    class InvalidRuleExeption(Exception):
        def __init__(self, rule: str) -> None:
            super().__init__(f"Invalid format of rule: {rule}")

    def __init__(self, rule: str) -> None:
        self.rule = rule
        if not self.__is_valid():
            raise Rule.InvalidRuleExeption(rule)
        self.head = self.__get_head()
        self.head_without_variables = remove_variables(self.head)
        self.tail = self.__get_tail()

    def __is_valid(self):
        # f(x, y) = (p(x) ~> v(x))
        # pattern = re.compile(r"^[a-z]\(([a-z],)*[a-z]\)=\([a-z]\([a-z]\)~>[a-z]\([a-z]\)\)$")
        # return bool(pattern.match(self.func))
        return True
    
    def __get_head(self):
        head_tail_pattern = r"^(.+)=(.*)$"
        return re.match(head_tail_pattern, self.rule).group(1)

    def __get_tail(self):
        head_tail_pattern = r"^(.+)=(.*)$"
        pairs_str = re.match(head_tail_pattern, self.rule).group(2)
        pairs_str=pairs_str[2:-2]
        pairs_lst = pairs_str.split("),(")
        dct = dict()
        for tupl in pairs_lst:
            ind_x, ind_y, value = tupl.split(",")
            dct[ind_x[1]]=dict()
        for tupl in pairs_lst:
            ind_x, ind_y, value = tupl.split(",")
            dct[ind_x[1]][ind_y[0]] = float(value)
        return dct
