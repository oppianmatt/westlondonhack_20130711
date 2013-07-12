from Levenshtein import distance
import random

#TARGET = 'CHISWICK'
TARGET = 'I HEART CHISWICK'
ABC = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
POP_SIZE = 20
#CYCLES = 100
#population = []

def mutate(string, n=1):
    result = list(string)
    for i in range(0, n):
        x = random.randrange(0, len(string))
        result[x] = givemestring(1)
    return "".join(result)

def givemestring(length):
    result = []
    for i in range(0, length):
        result.append(ABC[random.randrange(0, len(ABC))])
    return "".join(result)

def crossover(string1, string2):
    result = []
    for i in range(0, len(string1)):
        result.append(random.choice((string1[i], string2[i])))
    return "".join(result)

def givemepop(initialpop):
    result = initialpop
    for i in range(len(initialpop), POP_SIZE):
        s = givemestring(len(TARGET))
        d = distance(s, TARGET)
        result.append((d, s))
    result.sort()
    return result

def mate_pop(top, population):
    new_pop = []
    new_pop.append((distance(top, TARGET), top))
    for pair in population:
        string = mutate(crossover(pair[1], top))
        d = distance(string, TARGET)
        new_pop.append((d, string))
    new_pop.pop()
    new_pop.sort()
    return new_pop

def try2():
    # create initial
    population = []
    population = givemepop(population)
    print population
    top = population[0][1]
    count = 0
    while top != TARGET:
        print top
        #print population
        population = mate_pop(top, population)
        top = population[0][1]
        print count
        count += 1
    print top
    print count
    print population


def main():
    try2()
    return
    population = []
    population = givemepop(population)
    print population
    for i in range(0, CYCLES):

#    for i in range(0, POP_SIZE):
#        s = givemestring(len(TARGET))
#        d = distance(s, TARGET)
#        population.append((d, s))
#    population.sort()

        mated = crossover(population[0][1], population[1][1])
        d = distance(mated, TARGET)
        new_pop = []
        new_pop.append((d, mated))
        new_pop.append(population[0])
        new_pop.append(population[1])
#    for i in range(0, POP_SIZE - len(new_pop)):
#        s = givemestring(len(TARGET))
#        d = distance(s, TARGET)
#        new_pop.append((d, s))
#    new_pop.sort()
        new_pop = givemepop(new_pop)
        print new_pop
        population = new_pop

if __name__ == "__main__":
    main()