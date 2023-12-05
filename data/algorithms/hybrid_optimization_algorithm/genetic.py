import random

# Определение функции Розенброка
def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Создание начальной популяции
def create_population(min_x, max_x, min_y, max_y, population_size):
    return [(random.uniform(min_x, max_x), random.uniform(min_y, max_y)) for _ in range(population_size)]

# Вычисление пригодности (fitness) для каждой особи в популяции
def compute_fitness(population):
    fitness_scores = []
    for ind in population:
        x, y = ind
        fitness_scores.append(rosenbrock(x, y))
    return fitness_scores

# Селекция (выбор лучших особей)
def select_best_individuals(population, fitness_scores, num_parents):
    selected_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_parents]
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
def genetic_algorithm(population):
    population_size = len(population)
    # population = create_population(population_size)
    # best_individuals_per_generation = []

    fitness_scores = compute_fitness(population)
    parents = select_best_individuals(population, fitness_scores, population_size // 2)
    offspring = crossover(parents, population_size - len(parents))
    mutated_offspring = mutate(offspring)
    population = parents + mutated_offspring
        # best_fitness = min(fitness_scores)
        # best_individuals_per_generation.append((generation, best_fitness, min(population, key=lambda x: rosenbrock(x[0], x[1]))))
    return population


