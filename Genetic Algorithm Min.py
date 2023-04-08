#GENETİK ALGORİTMA (MIN)




import numpy as np
import random as rnd
import matplotlib.pyplot as plt
iterasyon = 10
crosover_rate = 0.50
pop_size = 8
gen_size = 5


def create_chromosome():
    return [rnd.randint(-10, 10) for x in range(0, gen_size)]


def create_initial_population():
    return [create_chromosome() for x in range(0, pop_size)]


def fitness(cr):
    return np.sin(cr[0]) + np.sin((10 / 3) * cr[0])


def probability(fitness_values):
    P = []
    total = sum(fitness_values)
    for f in fitness_values:
        P.append(f / total)
    return P


def crossover(p1, p2):
    print("crossover p1:", p1)
    print("crossover p2:", p2)
    o1 = []
    o2 = []
    c = rnd.randint(1, gen_size - 1)
    print("Cut point:", c)
    p1 = bin(int(p1[0])).replace("0b", "").zfill(gen_size)
    p2 = bin(int(p2[0])).replace("0b", "").zfill(gen_size)
    o1[:c] = p2[:c]
    o1[c:] = p1[c:]

    o2[:c] = p1[:c]
    o2[c:] = p2[c:]

    def convert_bin(y):
        s = [str(integer) for integer in y]
        a_string = "".join(s)
        res = int(a_string, 2)
        x = [res]
        return x

    o1 = convert_bin(o1)
    o2 = convert_bin(o2)
    return o1, o2


def mutasyon(mut):
    temp = mut[:]
    gen = rnd.randint(-10, 10)
    index = 0
    temp[index] = gen
    return temp


population = create_initial_population()
fitness_values = []

for c in population:
    fitness_values.append(fitness(c))
epok = 0
while epok < iterasyon:
    def grafik():
        iterasyon = [7, 6, 5, 4, 3, 2, 1, 0]
        plt.xlabel('POPULASYON')
        plt.ylabel('Fitness')
        plt.title('Fitness-Iterasyon Grafigi')
        plt.plot(iterasyon, fitness_values)
        plt.show()


    grafik()
    P = probability(fitness_values)

    C = np.cumsum(P)

    rulet_parents = []

    for i in range(0, len(C)):
        r = rnd.random()
        print("Random:", r)
        for j in range(0, len(C)):
            if C[j] > r:
                rulet_parents.append(j)
                break

    for c, f, p in zip(population, fitness_values, P):
        print(c, " ", f, " ", p)
    print(C)

    print(rulet_parents)

    crosover_parents = []
    k = 0
    while k < pop_size:
        r = rnd.random()
        if r < crosover_rate:
            if rulet_parents[k] not in crosover_parents:
                crosover_parents.append(rulet_parents[k])
        k = k + 1
    print("Caprazalnacak bireyler:", crosover_parents)

    if len(crosover_parents) >= 2:
        for i in range(0, len(crosover_parents)):
            for j in range(i + 1, len(crosover_parents)):
                o1, o2 = crossover(population[crosover_parents[i]]
                                   , population[crosover_parents[j]])
                population.append(o1)
                population.append(o2)
                fitness_values.append(fitness(o1))
                fitness_values.append(fitness(o2))

    else:
        print("Crossover icin yetrli birey gelmedi !!!")
    print("crossover sonrasi populasyon")
    for c, f in zip(population, fitness_values):
        print(c, " ", f)
    for r in range(0, 5):
        mut = mutasyon(population[rnd.randint(0, len(population) - 1)])

        population.append(mut)
        fitness_values.append(fitness(mut))

    print("mutasyon sonrasi populasyon")
    for c, f in zip(population, fitness_values):
        print(c, " ", f)

    zip_list = zip(fitness_values, population)

    sort_list = sorted(zip_list, reverse=False)

    for f, p in list(sort_list):
        print(f, " ", p)

    p = len(population)

    while p > pop_size:
        sort_list.pop()
        p = p - 1
    print("elitizm sonrasi")

    for f, p in list(sort_list):
        print(f, " ", p)

    population = []
    fitness_values = []

    for f, p in list(sort_list):
        population.append(p)
        fitness_values.append(f)
    epok += 1

print("Son populasyon")
for c, f in zip(population, fitness_values):
    print(c, " ", f)
print("En iyi birey:", population[1], " fitness:", fitness_values[1])
