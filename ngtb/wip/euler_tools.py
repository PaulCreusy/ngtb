###############
### Imports ###
###############

from math import sqrt, pow
from typing import Any
from numba import jit

###############
### Classes ###
###############


#################
### Fonctions ###
#################

### Dichotomie ###

@jit
def dichotomie(nb, l):
    a = 0
    b = len(l) - 1
    c = (a + b) // 2
    if nb > l[b]:
        return False
    while l[c] != nb and b - a > 1:
        if l[c] > nb:
            b = c
        else:
            a = c
        c = (a + b) // 2
    if l[c] == nb:
        return True
    return False

### Manipulation de chaines ###

def insert_car_in_str(chaine, car, pos):
    return chaine[:pos] + car + chaine[pos:]

def find_first_car_id(chaine, car):
    for i in range(len(chaine)):
        if chaine[i] == car:
            return i
    return -1

### Suite de Fibonnaci ###


fibo_memory = (2, 1, 1)

def fibo(n):
    global fibo_memory
    if n == 1 or n == 2:
        return 1
    if n > fibo_memory[0]:
        start, current, last = fibo_memory
    else:
        start = 2
        last = 1
        current = 1
    for i in range(start, n):
        last_last = last
        last = current
        current = last + last_last
    if n > fibo_memory[0]:
        fibo_memory = n, current, last
    return current

### Test de primalité ###

@jit
def test_prem(nb):
    if nb < 2:
        return False
    for i in range(2, int(sqrt(nb)) + 1):
        if i == nb:
            return True
        if nb % i == 0:
            return False
    return True

def test_prem_with_list(nb, l_prems):
    if nb < 2:
        return False
    for i in l_prems:
        if i > sqrt(nb):
            return True
        if nb % i == 0:
            return False
    return True

### Combinatory number generation ###


def generate_nb_from_comb_scheme_same_rep(scheme: str, replacer):
    l_numbers = []
    pile = [scheme.replace("_", str(replacer))]
    while len(pile) > 0:
        current_chaine = pile.pop()
        first_id = find_first_car_id(current_chaine, "#")
        if first_id != -1:
            for i in range(10):
                if i != replacer:
                    new_chaine = current_chaine.replace("#", str(i), 1)
                    pile.append(new_chaine)
        else:
            l_numbers.append(int(current_chaine))
    return l_numbers

def generate_nb_from_comb_scheme_same_env(scheme: str):
    l_numbers = []
    pile = [scheme]
    while len(pile) > 0:
        current_chaine = pile.pop()
        first_id = find_first_car_id(current_chaine, "#")
        if first_id != -1:
            for i in range(10):
                new_chaine = current_chaine.replace("#", str(i), 1)
                pile.append(new_chaine)
        else:
            l_numbers.append(current_chaine)
    res = [[] for i in range(10)]
    for i in range(10):
        for e in l_numbers:
            res[i].append(int(e.replace("_", str(i))))
    return res

def create_comb_scheme(k, n):
    l_scheme = []
    pile = [("_" * k, 0, 0)]
    stop = n - k
    while len(pile) > 0:
        current_chaine, current_state, current_start_idx = pile.pop()
        if current_state == stop:
            l_scheme.append(current_chaine)
        else:
            for i in range(current_start_idx, n):
                new_chaine = insert_car_in_str(current_chaine, "#", i)
                new_start_idx = current_start_idx + i + 1
                pile.append((new_chaine, current_state +
                            1, new_start_idx))
    return l_scheme
