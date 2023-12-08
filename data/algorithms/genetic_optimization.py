# arr-points - массив пар точек x и y

import random


# Создание начальной популяции
def create_population(population_size):
    return [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(population_size)]


# Вычисление пригодности (fitness) для каждой особи в популяции
def compute_fitness(func, population):
    fitness_scores = []
    for ind in population:
        x, y = ind
        fitness_scores.append(func(x, y))
    return fitness_scores


# Селекция (выбор лучших особей)
# def select_best_individuals(population, fitness_scores, num_parents):
#     selected_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_parents]
#     return [population[i] for i in selected_indices]

# Селекция турнирным методом (выбор лучших особей)
def select_best_individuals_tournament(population, fitness_scores, num_parents, tournament_size=2):
    selected_indices = []
    for parent in range(num_parents):
        tournament_indices = random.sample(range(len(fitness_scores)), tournament_size)
        tournament_fitness = [fitness_scores[i] for i in tournament_indices]
        winner_index = tournament_indices[tournament_fitness.index(min(tournament_fitness))]
        selected_indices.append(winner_index)
    return [population[i] for i in selected_indices]

# Скрещивание (кроссовер)
def crossover(parents, offspring_size):
    offspring = []
    while len(offspring) < offspring_size:
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        offspring.append(child)
    return offspring


# Мутация
def mutate(offspring):
    mutated_offspring = []
    for child in offspring:
        x, y = child
        if random.random() < 0.1:  # Вероятность мутации
            x += random.uniform(-0.5, 0.5)
            y += random.uniform(-0.5, 0.5)
        mutated_offspring.append((x, y))
    return mutated_offspring


# Генетический алгоритм
def genetic_algorithm(func, population_size, num_generations):
    population = create_population(population_size)
    arr_points = []
    population_list = []
    for generation in range(num_generations):
        fitness_scores = compute_fitness(func, population)
        # parents = select_best_individuals(population, fitness_scores, population_size // 2)
        parents = select_best_individuals_tournament(population, fitness_scores, population_size // 2)
        offspring = crossover(parents, population_size - len(parents))
        mutated_offspring = mutate(offspring)
        population = parents + mutated_offspring

        # Вывод популяции
        # for item in population:
        #     population_list.append([item[0], item[1], fitness_scores]
        #     )

        # best_fitness = min(fitness_scores)
        # print(f"Поколение {generation + 1}: Лучшее значение функции Розенброка = {best_fitness}")
        arr_points.append([population[fitness_scores.index(min(fitness_scores))][0], population[fitness_scores.index(min(fitness_scores))][1], min(fitness_scores)])

    best_solution = population[fitness_scores.index(min(fitness_scores))]
    return best_solution, min(fitness_scores), arr_points
