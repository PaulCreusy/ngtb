import numpy as np
from tqdm import tqdm

def differential_evolution(cost_function, lower_bound_array: np.array, upper_bound_array: np.array, generations_number=100, population_size=None, scaling_factor=0.8, crossover_probability=0.7):
    """
    Differential evolution algorithm
    """

    ### Initialisation ###

    # Raise error if dimensions of lower and upper array do not match
    if len(upper_bound_array) != len(lower_bound_array):
        raise ValueError(
            "The dimensions of both bound arrays are not matching.")

    # Extract dimension of the problem
    dimension = len(upper_bound_array)

    # Set the size of the population if none is given
    if population_size is None:
        population_size = int(10 + np.sqrt(dimension))

    # Initialise matrixes
    cost_matrix = np.zeros((population_size, generations_number))
    population_matrix = np.zeros(
        (population_size, dimension))

    # Create a random start population
    population_matrix = np.transpose(np.repeat(np.expand_dims(lower_bound_array, -1), population_size, 1) + np.repeat(
        np.expand_dims(upper_bound_array - lower_bound_array, -1), population_size, 1)) * np.random.random((population_size, dimension))

    # Compute the cost associated to the start population
    for i in range(population_size):
        cost_matrix[i, 0] = cost_function(population_matrix[i, :])

    ### Main loop ###

    for gen_id in tqdm(range(generations_number - 1)):

        for i in range(population_size):

            ## Mutation step ##

            # Choose three individuals of the population excluding the current one
            vector_choice = np.random.randint(0, population_size - 2, (3,))
            vector_choice[vector_choice >= 1] += 1
            a, b, c = population_matrix[vector_choice, :]

            # Apply the mutation
            mutation_vector = a + scaling_factor * (b - c)

            ## Crossover step ##

            # Creation of the crossover vector
            crossover_vector = (np.random.random(
                (dimension,)) <= crossover_probability)

            # Apply the crossover to select the trials
            trial_vector = crossover_vector * \
                mutation_vector + (1 - crossover_vector) * \
                population_matrix[i, :]

            ## Selection step ##

            # Apply the boundaries
            trial_vector = np.minimum(trial_vector, upper_bound_array)
            trial_vector = np.maximum(trial_vector, lower_bound_array)

            # Keep the best vector
            trial_cost = cost_function(trial_vector)
            if trial_cost < cost_matrix[i, gen_id]:
                population_matrix[i, :] = trial_vector
                cost_matrix[i, gen_id + 1] = trial_cost
            else:
                cost_matrix[i, gen_id + 1] = cost_matrix[i, gen_id]

    best_id = np.argmin(cost_matrix[:, -1])
    best_vector = population_matrix[best_id, :]

    return best_vector
