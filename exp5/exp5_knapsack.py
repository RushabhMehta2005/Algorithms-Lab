import csv
import random
import os

class Item:
    def __init__(self, value, weight, shelf_life):
        self.value = value
        self.weight = weight
        self.shelf_life = shelf_life
        self.ratio = value / (weight * shelf_life)

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
    print(f"File {i} - Maximum value: {max_value_greedy}")
