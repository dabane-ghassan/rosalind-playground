def dH(s : str, t : str) -> int : 
    return sum([pos1 != pos1prime for pos1, pos1prime in zip(s,t)])

# Test 
s_ex = "GAGCCTACTAACGGGAT"
t_ex = "CATCGTAATGACGGCCT"

print(dH(s_ex, t_ex))