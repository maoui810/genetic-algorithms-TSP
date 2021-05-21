import random
import time
from itertools import permutations

import numpy as np

starting_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("start State Check")
print(starting_state)
holdRandom = []
# original matrix gride
distanceMatrix = np.array(
    [
        [0, 2, 11, 3, 18, 14, 20, 12, 5], [2, 0, 13, 10, 5, 3, 8, 20, 17],
        [11, 13, 0, 5, 19, 21, 2, 5, 8], [3, 10, 5, 0, 6, 4, 12, 15, 1],
        [18, 5, 19, 6, 0, 12, 6, 9, 7], [14, 3, 21, 4, 12, 0, 19, 7, 4],
        [20, 8, 2, 12, 6, 19, 0, 21, 13], [12, 20, 5, 15, 9, 7, 21, 0, 6],
        [5, 17, 8, 1, 7, 4, 13, 6, 0]
    ]
)


# permutation, distance = solve_tsp_dynamic_programming(distanceMatrix)

# make Population
def Create_poplation(n, starting_state):
    initial_pop = []
    perm = list(permutations(starting_state))
    for i in range(0, n):
        initial_pop.append(random.choice(perm))
    # print(initial_pop)
    return initial_pop


def func(starting_state):
    # calulate the distance
    curr = 0
    for i in range(0, len(starting_state) - 1):
        curr += distanceMatrix[starting_state[i] - 1][starting_state[i + 1] - 1]

    curr = curr + distanceMatrix[starting_state[8] - 1][starting_state[0] - 1]

    return curr


print(func(starting_state))


def Random_slec(population, func, pCheck):
    total = 0
    for i in population:
        total += func(i)

    x = 0
    # if randomly selected Fit parent is selected it wont be selected again for reproduction
    # HoldRandom holds all the choosen parents so they are not selected again

    if pCheck not in holdRandom:
        for i in population:
            # Choose radom parent divide its fitness value by total poplulation distance value
            RandomPIcked2 = random.choice(population)
            firstValue = func(RandomPIcked2)
            # print(firstValue)
            percent = firstValue / total
            # choose another Parent Dvide its fitness value by total
            RandomPIcked = random.choice(population)

            valueHold = func(RandomPIcked)
            # print(valueHold)
            compare = valueHold / total
            # print(f"percentage : {percent}")
            # If first parents fintness overall better than choose that parent other wise pick another random parent
            if compare < percent:
                # print(f'YEEE WE GOT Picked: {valueHold} and here is the Parent that was choosen: {RandomPIcked} and y element was {firstValue}')
                picked = RandomPIcked
                holdRandom.append(picked)
                break


    else:
        Random_slec(population, func, pCheck)

    return picked, func(picked)


def Reproudce(x, y):
    # choose 3 elemetns out of X parent
    sample = random.sample(x, 3)

    child = []
    # combine parent y and choosen elements from x to form new Child
    for i in range(0, len(y)):
        if i + 1 not in sample:
            child.append(i + 1)
    child = child + sample
    return child


# Muate a Child
def swapPositions(list_C):
    num1 = random.randrange(5, 8)
    num2 = random.randrange(4)
    pos1, pos2 = num1, num2
    list_C[pos1], list_C[pos2] = list_C[pos2], list_C[pos1]
    return list_C


def FindBestFit(population):
    # 2d list holds Path to cities and Distance per path
    rows, cols = (len(population), 1)
    arr = []

    for i in population:

        col = []
        for j in range(cols):
            col.append(i)
            col.append(func(i))

        arr.append(col)

    # sorts by second element in 2D list which is distance so first element would be the most fit
    arr.sort(key=lambda x: x[1])

    return arr[0]


def GeneticAl(population, Generations):
    Start = time.time()
    print("Genetic Algorithm Started")
    for j in range(0, Generations):

        newPopulation = []
        cout = 0

        for i in population:
            pCheck = holdRandom
            # grab random Parents 1 and 2
            x = Random_slec(population, func, pCheck)
            jamx = list(x[0])
            y = Random_slec(population, func, pCheck)
            jamyy = list(y[0])

            # send parents to Reproduce a Child
            chiloffspring = Reproudce(jamx, jamyy)

            # Chance of Random Muation of Child else add new offspring to new population list and overall Population list
            if random.uniform(0, 1) > .85:
                cout += 1
                muatedchild = swapPositions(chiloffspring)
                newPopulation.append(muatedchild)
                TotalMostFit.append(muatedchild)
            else:
                newPopulation.append(chiloffspring)
                TotalMostFit.append(chiloffspring)

        print(f'Ouf of Populatin of : {len(newPopulation)} and Mutated Childeren: {cout} ')
        print(f'Generation {j} Best Result:{FindBestFit(newPopulation)}')
    end = time.time()

    print(f'Time Taken to Run: {end - Start}')
    return FindBestFit(TotalMostFit)


population = Create_poplation(1000, starting_state)
Generations = 10
# holds all the genrations
TotalMostFit = []

print("_______________________________________________________________________________________")

print(f'Best Result Overall out of all the generations: {GeneticAl(population, Generations)}')
print('*************************************************************************************')
print(f'Generations : {Generations} Length of all Populations in Total {len(TotalMostFit)}')
