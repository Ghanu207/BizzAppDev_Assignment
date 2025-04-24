# Approach:
# 1. Treat the problem as a circular permutation challenge.
# 2. Generate all permutations of guest seating.
# 3. For each permutation, check if every guest has their two preferred neighbors adjacent in the circle.
# 4. Return the first valid arrangement or report that no valid arrangement exists.

from itertools import permutations

def is_valid_arrangement(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left_neighbor = arrangement[(i - 1) % n]
        right_neighbor = arrangement[(i + 1) % n]
        if not (left_neighbor in preferences[guest] and right_neighbor in preferences[guest]):
            if not (right_neighbor in preferences[guest] and left_neighbor in preferences[guest]):
                return False
    return True

def find_seating_arrangement(preferences):
    guests = list(preferences.keys())
    for perm in permutations(guests):
        if is_valid_arrangement(perm, preferences):
            return list(perm)
    return None

# Example input
guests_preferences = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

# Run the function
arrangement = find_seating_arrangement(guests_preferences)

# Output the result
if arrangement:
    print("Valid seating arrangement found:")
    print(" -> ".join(arrangement))
else:
    print("No valid seating arrangement is possible.")
