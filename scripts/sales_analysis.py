import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

data = []
with open('data/restaurant.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

state_sales = defaultdict(float)

for row in data[1:]:
    state = row[5]
    sales = float(row[2])
    state_sales[state] += sales

sorted_states = sorted(state_sales.items(), key=lambda x: x[1], reverse=True)

if not os.path.exists('results'):
    os.mkdir('results')

# Save the results in the results folder
with open('results/sales_results.txt', 'w') as file:
    for state, total_sales in sorted_states:
        file.write(f"State: {state}, Total Sales: {total_sales}\n")

# Extract state names and corresponding total sales for bar chart
states = [state[0] for state in sorted_states]
total_sales = [state[1] for state in sorted_states]

# Create and save the bar chart
plt.figure(figsize=(10, 6))
plt.bar(states, total_sales, color='skyblue')
plt.xlabel('States')
plt.ylabel('Total Sales')
plt.title('Total Sales by State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/sales_results_chart.png')  
plt.show()


