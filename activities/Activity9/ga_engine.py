"""A simple, non-elitist Genetic Algorithm for the packing problem
(Session 16), plus a brute-force ground truth for comparison.

This follows the "simple genetic algorithm" (AGS) described in the course
material: fixed population size, proportional (roulette) selection,
one-point crossover with fixed probability, uniform mutation with fixed
probability, and NON-elitist selection — meaning the best individual found
so far is not automatically protected from one generation to the next. That
is exactly why the algorithm (both here and in the course's own pseudocode)
tracks a separate "best-ever" value across all generations.

Everything here is deterministic: a fixed random seed means every student
who runs the app sees the exact same population, the exact same
generation-by-generation results, and the exact same final answer.
"""

import itertools
import random

from ga_data import CAPACITY_KG, ITEMS, NUM_ITEMS, fitness, weight_and_value

SEED = 84
POPULATION_SIZE = 8
GENERATIONS = 12
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.05

Chromosome = tuple[int, ...]


def _select_one(rng: random.Random, population: list[Chromosome], fits: list[int]) -> Chromosome:
    """Roulette-wheel selection, proportional to fitness. Falls back to a
    uniform random pick if every individual in the population is infeasible
    (total fitness 0), since roulette can't work with nothing to weigh.
    """
    total = sum(fits)
    if total == 0:
        return rng.choice(population)
    pick = rng.uniform(0, total)
    running = 0
    for individual, f in zip(population, fits):
        running += f
        if running >= pick:
            return individual
    return population[-1]


def _crossover(rng: random.Random, parent1: Chromosome, parent2: Chromosome) -> tuple[Chromosome, Chromosome]:
    """One-point crossover (Session 16: 'crossing at one point')."""
    if rng.random() < CROSSOVER_PROB:
        point = rng.randint(1, NUM_ITEMS - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2


def _mutate(rng: random.Random, chromosome: Chromosome) -> Chromosome:
    """Uniform mutation: every bit independently has the same small chance
    of flipping."""
    return tuple((1 - bit) if rng.random() < MUTATION_PROB else bit for bit in chromosome)


def run_ga() -> list[dict]:
    rng = random.Random(SEED)
    population = [tuple(rng.randint(0, 1) for _ in range(NUM_ITEMS)) for _ in range(POPULATION_SIZE)]

    history = []
    best_ever_chromosome: Chromosome | None = None
    best_ever_fitness = -1

    for gen in range(1, GENERATIONS + 1):
        fits = [fitness(ind) for ind in population]
        gen_best_idx = max(range(POPULATION_SIZE), key=lambda i: fits[i])
        gen_best_chromosome = population[gen_best_idx]
        gen_best_fitness = fits[gen_best_idx]

        if gen_best_fitness > best_ever_fitness:
            best_ever_fitness = gen_best_fitness
            best_ever_chromosome = gen_best_chromosome

        history.append(
            {
                "generation": gen,
                "population": list(population),
                "fitnesses": list(fits),
                "gen_best_chromosome": gen_best_chromosome,
                "gen_best_fitness": gen_best_fitness,
                "best_ever_chromosome": best_ever_chromosome,
                "best_ever_fitness": best_ever_fitness,
            }
        )

        new_population: list[Chromosome] = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = _select_one(rng, population, fits)
            parent2 = _select_one(rng, population, fits)
            child1, child2 = _crossover(rng, parent1, parent2)
            new_population.append(_mutate(rng, child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(_mutate(rng, child2))
        population = new_population

    return history


def brute_force_optimum() -> tuple[int, Chromosome]:
    """Ground truth: tries every possible packing (2^8 = 256 combinations)
    and returns the best feasible one. Used only to check how close the GA
    got — the GA itself never sees this.
    """
    best_value = -1
    best_chromosome: Chromosome = tuple([0] * NUM_ITEMS)
    for bits in itertools.product([0, 1], repeat=NUM_ITEMS):
        weight, value = weight_and_value(bits)
        if weight <= CAPACITY_KG and value > best_value:
            best_value = value
            best_chromosome = bits
    return best_value, best_chromosome


HISTORY = run_ga()
OPTIMAL_VALUE, OPTIMAL_CHROMOSOME = brute_force_optimum()
