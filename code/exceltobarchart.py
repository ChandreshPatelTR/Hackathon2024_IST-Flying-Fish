import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
bar_data = pd.read_csv('feature_event.csv').head(10)
# Create a line chart
plt.figure(figsize=(8, 8))
plt.bar(bar_data['NUM_EVENTS'], bar_data['NUM_MINUTES'], color='skyblue')
plt.title('NUM_EVENTS NUM_MINUTES Bar Chart')
plt.xlabel('NUM_EVENTS')
plt.ylabel('NUM_MINUTES')
plt.grid(True) 
plt.show()