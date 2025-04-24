
"""
Approach:
1. Sort tasks by deadline.
2. Use a greedy algorithm with a min-heap to keep track of durations of selected tasks.
3. If the total time exceeds the deadline, drop the longest task to stay within limits.
"""

import heapq

def max_tasks(tasks):
    # Sort tasks by their deadline
    tasks.sort(key=lambda x: x['deadline'])
    total_time = 0
    min_heap = []

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']
        heapq.heappush(min_heap, -duration)  # use negative for max heap behavior
        total_time += duration

        if total_time > deadline:
            # Remove the task with the longest duration
            total_time += heapq.heappop(min_heap)  # add because popped is negative

    return len(min_heap)

# Example input
tasks_list = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

# Output
print("Maximum number of tasks that can be completed:", max_tasks(tasks_list))
