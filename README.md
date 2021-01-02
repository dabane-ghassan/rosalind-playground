# My ROSALIND playground 
My personal ROSALIND playground to practice some bioinformatics problems during my freetime (and while listening to some Eminem at the same time).

## Topics

Topics are taken from the official ROSALIND problem collection [here](http://rosalind.info/problems/topics/)..

### Alignement

#### HAMM - Counting point mutations

- The Hamming Distance <img src="https://render.githubusercontent.com/render/math?math=d_H(s,t)">

- with Python :
  
```python
def dH(s: str, t: str) -> int : 
    return sum([pos != pos_prime for pos, pos_prime in zip(s,t)])
```

#### TRAN -  Transitions and Transversions

- The Transition/Transversion Ratio <img src="https://render.githubusercontent.com/render/math?math=R(s_1,s_2)">

- with Python :
  
```python
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
```

### Combinatorics

### Computational Mass Spectrometry

### Divide-and-conquer

### Dynamic Programming

### Genome Assembly

### Genome Rearrangements

### Graph Algorithms

### Graphs

### Heredity

### Phylogeny

### Population Dynamics

### Probability 

### Set Theory

### Sorting

### String Algorithms

