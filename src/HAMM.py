def dH(s: str, t: str) -> int : 
    return sum([pos != pos_prime for pos, pos_prime in zip(s,t)])

# Test 
s_ex = "GAGCCTACTAACGGGAT"
t_ex = "CATCGTAATGACGGCCT"

print(dH(s_ex, t_ex))