import csv
import os
import matplotlib.pyplot as plt

# Read the data from CSV file
data = []
with open('data/restaurant.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Extract meal quantities
meal_quantities = [int(float(row[6])) for row in data[1:]]

# Create and save the histogram
plt.figure(figsize=(10, 6))
plt.hist(meal_quantities, bins=20, color='skyblue')
plt.xlabel('Meal Quantities')
plt.ylabel('Frequency')
plt.title('Distribution of Meal Quantities Served by Restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/meal_results_histogram.png') 
plt.show()
