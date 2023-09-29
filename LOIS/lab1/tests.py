from src.operations import *
from src.data_validators import fact_is_valid
from src.data_loader import load_from_file


assert(conjunction({"x": 0.1, "y": 1, "z": 0, "f": 0.4}, {"x": 0.5, "y": 0, "z": 0.2, "d": 0.5})== {"x": 0.5, "y":1,"z":0.2, "f":0.4, "d": 0.5})
assert(disjunction({"x": 0.1, "y": 1, "z": 0, "f": 0.4}, {"x": 0.5, "y": 0, "z": 0.2, "d": 0.5})=={"x": 0.1, "y": 0, "z": 0})
assert(difference({"x": 0.1, "y": 1, "z": 0, "f": 0.4}, {"x": 0.5, "y": 0, "z": 0.2, "d": 0.5})=={"x": 0, "y":1,"z":0, "f": 0.4})


assert(fact_is_valid("p(x)={(a,0),(b,0.3),(c,1)}") == True)
assert(fact_is_valid("(x)={(a,0),(b,0.3),(c,1)}") == False)
assert(fact_is_valid("p={(a,0),(b,0.3),(c,1)}") == False)
assert(fact_is_valid("p={(a,0),(b,0.3)(c,1)}") == False)
# assert(fact_is_valid("p={}") == True) # ? -- False 

    
