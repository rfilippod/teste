import numpy as np

def rkga(matrix, population_size, num_generations, mutation_rate):
    num_rows, num_cols = matrix.shape

    # Define the fitness function
    def fitness(random_key):
        schedule = np.zeros((num_rows, num_cols))
        index = 0
        for row in range(num_rows):
            for col in range(num_cols):
                schedule[row, col] = random_key[index]
                index += 1
        fitness = np.sum(schedule * matrix)
        return fitness

    # Initialize the population
    population = []
    for i in range(population_size):
        random_key = np.random.permutation(num_rows * num_cols)
        population.append(random_key)

    # Run the evolution loop
    for generation in range(num_generations):
        # Evaluate the fitness of each individual
        fitness_values = [fitness(random_key) for random_key in population]

        # Select the parents for the next generation
        parent_indices = np.random.choice(population_size, size=population_size, replace=True, p=fitness_values / sum(fitness_values))

        # Generate the offspring for the next generation
        offspring = []
        for i in range(population_size):
            parent1 = population[parent_indices[i]]
            parent2 = population[np.random.choice(population_size)]
            crossover_point = np.random.randint(num_rows * num_cols)
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            mutation_mask = np.random.rand(num_rows * num_cols) < mutation_rate
            mutation = np.random.permutation(np.where(mutation_mask)[0])
            child[mutation] = np.random.permutation(num_rows * num_cols)[:len(mutation)]
            offspring.append(child)

        # Replace the current population with the offspring
        population = offspring

    # Find the best individual in the final population
    best_individual = max(population, key=fitness)

    return best_individual


matrix = np.array([[1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 1, 0, 0],
                   [0, 0, 1, 1]])

population_size = 100
num_generations = 100
mutation_rate = 0.01

best_random_key = rkga(matrix, population_size, num_generations, mutation_rate)

print('Best random key:', best_random_key)