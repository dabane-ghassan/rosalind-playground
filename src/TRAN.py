from itertools import permutations

def R(s1: str, s2: str) -> int : 
    
    transitions = set(
        [("A","G"), ("G","A"), ("C","T"), ("T","C")]
        ) # all possible transitions
    transversions = set(
        permutations(["A","G","C","T"],2)
        ) - transitions  # all possible transversions

    n_trans, n_tranv = 0, 0
    for pos, pos_prime in zip(s1_ex, s2_ex) :
        if pos != pos_prime : 
            if (pos,pos_prime) in transitions :
                n_trans += 1
            elif (pos,pos_prime) in transversions : 
                n_tranv += 1
    return n_trans/n_tranv

s1_ex = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2_ex = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

print(R(s1_ex, s2_ex))

