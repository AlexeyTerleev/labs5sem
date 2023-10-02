def impl(v1, v2):
    if v1 <= v2:
        return 1.0
    else:
        return v2


def compute_impl(set1, set2):
    relation = {}
    for i in set1:
        relation[i] = {}
        for j in set2:
            v1 = set1[i]
            v2 = set2[j]
            relation[i][j] = impl(v1, v2)
    return relation


def conjunction(set1, set2):
    tmp_set = {x: max(y, set2.get(x, 0)) for x, y in set1.items()}
    for x, y in set2.items():
        if x not in tmp_set:
            tmp_set[x] = y
    return tmp_set
    
    
def disjunction(set1, set2):
    return {x: min(y, set2[x])  for x, y in set1.items() if x in set2}
    
    
def difference(set1, set2):
    res = {}
    for x, y in set1.items():
        res[x] = y - set2.get(x, 0) if y - set2.get(x, 0) > 0 else 0
    return res


def sim_diff(set1, set2):
    return conjunction(disjunction(set1, set2), disjunction(set2, set1))


def neg(set1):
    return {x: 1 - y for x, y in set1}
