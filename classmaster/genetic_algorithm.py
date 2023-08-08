import random

# Define your classes here (Timeslot, Subject, Faculty)

def initialize_population(pop_size, faculties, days, slot_availability):
    population = []
    for _ in range(pop_size):
        timetable = {}
        for faculty in faculties:
            faculty_slots = []
            for subject in faculty.subjects:
                if subject.is_practical:
                    slot_duration = 2  # Double the duration for practical
                else:
                    slot_duration = 1

                available_slots = [slot for slot, availability in slot_availability.items() if slot_duration <= availability]
                if available_slots:
                    chosen_slot = random.choice(available_slots)
                    faculty_slots.append((subject, chosen_slot))
                    for i in range(slot_duration):
                        slot_availability[chosen_slot + i] -= slot_duration

            timetable[faculty.name] = faculty_slots
        population.append(timetable)
    return population

# Define the rest of the Genetic Algorithm functions (fitness_function, selection, crossover, mutation)
def fitness_function(timetable):
    clashes = 0
    for faculty_slots in timetable.values():
        slots = set()
        for _, slot in faculty_slots:
            if slot in slots:
                clashes += 1
            slots.add(slot)
    fitness_score = 1 / (1 + clashes)  # Inverse of the number of clashes
    return fitness_score
def selection(population, fitness_scores, num_parents):
    selected_parents = []

    for _ in range(num_parents):
        tournament_size = 3  # Number of individuals in each tournament
        tournament_candidates = random.sample(range(len(population)), tournament_size)

        # Choose the candidate with the highest fitness score as the parent
        winner = min(tournament_candidates, key=lambda idx: fitness_scores[idx])
        selected_parents.append(population[winner])

    return selected_parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = {faculty: slots for faculty, slots in parent1.items()[:crossover_point]}
    offspring2 = {faculty: slots for faculty, slots in parent2.items()[:crossover_point]}
    
    for faculty, slots in parent2.items()[crossover_point:]:
        offspring1[faculty] = slots
    for faculty, slots in parent1.items()[crossover_point:]:
        offspring2[faculty] = slots
    
    return offspring1, offspring2
def mutation(timetable):
    mutated_timetable = timetable.copy()
    faculties = list(mutated_timetable.keys())
    faculty = random.choice(faculties)
    
    if mutated_timetable[faculty]:
        slot1 = random.choice(mutated_timetable[faculty])
        slot2 = random.choice(mutated_timetable[faculty])
        
        mutated_timetable[faculty].remove(slot1)
        mutated_timetable[faculty].remove(slot2)
        mutated_timetable[faculty].append(slot1)
        mutated_timetable[faculty].append(slot2)
    
    return mutated_timetable

def genetic_algorithm(faculties, days, slot_availability, pop_size=100, num_generations=100, num_parents=50, mutation_rate=0.1):
    population = initialize_population(pop_size, faculties, days, slot_availability)

    for generation in range(num_generations):
        fitness_scores = [fitness_function(timetable) for timetable in population]
        parents = selection(population, fitness_scores, num_parents)
        offspring = crossover(parents, pop_size - num_parents)
        for i in range(num_parents, pop_size):
            if random.random() < mutation_rate:
                offspring[i] = mutation(offspring[i], mutation_rate)
        population = parents + offspring

    best_timetable = max(population, key=lambda x: fitness_function(x))
    return best_timetable
