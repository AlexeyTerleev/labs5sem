def gedel_impl(v1, v2):
    return 1 if v1 <= v2 else v2


def matrix_impl(set1, set2):
    return {i: {j: gedel_impl(set1[i], set2[j]) for j in set2} for i in set1}


def t_norm(v1, v2):
    return min(v1, v2)


def built_impl_table(set1, relation):
    if set(set1.keys()) != set(relation.keys()):
        raise ValueError(f"{set(set1.keys())} != {set(relation.keys())}")
    return {i: {j: t_norm(set1[i], relation[i][j]) for j in relation[i]} for i in relation}


def compress(impl_table):
    row_keys = list(impl_table.keys())
    col_keys = list(impl_table[row_keys[0]].keys())
    return {col_key: max([impl_table[row_key][col_key] for row_key in row_keys]) for col_key in col_keys}


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
