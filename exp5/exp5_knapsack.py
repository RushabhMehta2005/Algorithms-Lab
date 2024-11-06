import csv
import random
import time
from itertools import combinations
import os

class Item:
    def __init__(self, value, weight, shelf_life):
        self.value = value
        self.weight = weight
        self.shelf_life = shelf_life
        self.ratio = value / weight  # Value-to-weight ratio

def generate_csv_files(num_files=5, num_items=20, folder="items_data"):
    os.makedirs(folder, exist_ok=True)
    for i in range(num_files):
        with open(f"{folder}/items_{i+1}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["value", "weight", "shelf_life"])
            for _ in range(num_items):
                value = random.randint(10, 100)
                weight = random.randint(1, 20)
                shelf_life = random.randint(1, 10)
                writer.writerow([value, weight, shelf_life])


def read_items_from_csv(file_path):
    items = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(Item(int(row["value"]), int(row["weight"]), int(row["shelf_life"])))
    return items


def greedy_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.ratio * capacity
            break
    return total_value


def brute_force_knapsack(items, capacity):
    start_time = time.time()
    max_value = 0
    n = len(items)
    for r in range(1, n + 1):
        for combo in combinations(items, r):
            if time.time() - start_time > 25:
                raise TimeoutError("Brute force solution time limit exceeded.")
            total_weight = sum(item.weight for item in combo)
            total_value = sum(item.value for item in combo)
            if total_weight <= capacity:
                max_value = max(max_value, total_value)
    return max_value

# Generate CSV files
generate_csv_files(num_files=5, num_items=20)

# Set knapsack capacity
capacity = 200

# Process each file individually
folder = "items_data"
for i in range(1, 6):
    file_path = f"{folder}/items_{i}.csv"
    items = read_items_from_csv(file_path)
    
    max_value_greedy = greedy_knapsack(items, capacity)
    max_value_greedy = round(max_value_greedy, 3)
    print(f"File {i} - Maximum value (Greedy): {max_value_greedy}")
    
    try:
        max_value_brute_force = brute_force_knapsack(items, capacity)
        max_value_brute_force = round(max_value_brute_force, 3)
        print(f"File {i} - Maximum value (Brute Force): {max_value_brute_force}")
    except TimeoutError as e:
        print(f"File {i} - Brute force solution: {e}")
