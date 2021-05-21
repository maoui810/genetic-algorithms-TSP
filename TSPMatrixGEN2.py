import time
import timeit
from collections import OrderedDict
from itertools import permutations
import sys
import random
from math import floor
from sys import maxsize
import numpy as np










starting_state =[1,2,3,4,5,6,7,8,9]
print("start State Check")
print(starting_state)
holdRandom=[]

distanceMatrix = np.array(
            [
            [0, 2, 11, 3, 18, 14, 20, 12, 5], [2, 0, 13, 10, 5, 3, 8, 20, 17],
             [11, 13, 0, 5, 19, 21, 2, 5, 8], [3, 10, 5, 0, 6, 4, 12, 15, 1],
             [18, 5, 19, 6, 0, 12, 6, 9, 7], [14, 3, 21, 4, 12, 0, 19, 7, 4],
             [20, 8, 2, 12, 6, 19, 0, 21, 13], [12, 20, 5, 15, 9, 7, 21, 0, 6],
             [5, 17, 8, 1, 7, 4, 13, 6, 0]
             ]
)

#permutation, distance = solve_tsp_dynamic_programming(distanceMatrix)


def Create_poplation(n,starting_state):
    perm=[]
    initial_pop=[]
    perm=list(permutations(starting_state))
    for i in range (0,n):
        initial_pop.append(random.choice(perm))
    #print(initial_pop)
    return initial_pop


def func(starting_state):

    curr=0
    for i in range (0, len(starting_state)-1):
        curr +=distanceMatrix[starting_state[i]-1][starting_state[i+1]-1]

    curr=curr+distanceMatrix[starting_state[8]-1][starting_state[0]-1]


    return curr

print(func(starting_state))








def Random_slec(population,func,pCheck):
    total = 0
    for i in population:
        total += func(i)

    y = 0
    x = 0

    if pCheck not in holdRandom:
        for i in population:
            y = func(i)

            percent = y / total
            RandomPIcked = random.choice(population)

            valueHold = func(RandomPIcked)
            compare = valueHold / total
            #print(f"percentage : {percent}")
            if compare < percent:
                #print(f'YEEE WE GOT Picked: {valueHold} and here is the Parent that was choosen: {RandomPIcked} and y element was {y}')
                picked=RandomPIcked
                holdRandom.append(picked)
                break


    else:Random_slec(population,func,pCheck)

    return picked,func(picked)




def Reproudce(x,y):

    sample = random.sample(x, 3)

    n = random.randint(0, len(y) - 3)

    child = []
    j = 0
    for i in range(0, len(y)):
        if i + 1 not in sample:
            child.append(i + 1)
    child = child + sample
    return child






def swapPositions(list_C):
    num1 = random.randrange(5, 8)
    num2 = random.randrange(4)
    pos1, pos2 = num1, num2
    list_C[pos1], list_C[pos2] = list_C[pos2], list_C[pos1]
    return list_C

def FindBestFit(population):
    rows, cols = (len(population), 1)
    arr = []


    for i in population:


        col = []
        for j in range(cols):
            col.append(i)
            col.append(func(i))

        arr.append(col)


    arr.sort(key=lambda x: x[1])

    print(arr[0])
    return arr[0]

#print(swapPositions(chiloffspring))

#print(func(chiloffspring))
population=Create_poplation(500,starting_state)
Generations=5
print("Orginal Population")
print(len(population))
def GeneticAl(population, Generations):
    Start = time.time()
    print("Genetic Algorithm Started")
    for j in range(0,Generations):

        newPopulation=[]
        cout=0

        for i in population:
            pCheck = holdRandom

            x = Random_slec(population, func, pCheck)
            jamx = list(x[0])
            y = Random_slec(population, func, pCheck)
            jamyy = list(y[0])

            chiloffspring = Reproudce(jamx, jamyy)
            if random.uniform(0, 1) > .8:
                cout +=1
                newPopulation.append(swapPositions(chiloffspring))
            else:
                newPopulation.append(chiloffspring)





        print(f'Child out of Population size {len(newPopulation)} and Mutated Childeren: {cout} ')
        print(f'Generation {j} Best Result:{FindBestFit(newPopulation)}')
    end = time.time()
    print(end - Start)
    return FindBestFit(newPopulation)


print("Best Route--------------- and Sortest Distance: ")
print(GeneticAl(population,Generations))
print(f'Best Results out of Generations: {Generations} and Poulation Size of: {len(population)}')
