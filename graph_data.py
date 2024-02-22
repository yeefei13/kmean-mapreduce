import matplotlib.pyplot as plt

# Function to read data from a file
def read_data(file_path):
    x, y = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x_value, y_value = line.strip().split(',')
            x.append(float(x_value))
            y.append(float(y_value))
    return x, y

# Read data points
data_x, data_y = read_data('dataset.txt')

# Read centroids
centroid_x, centroid_y = read_data('output\mapreduce-output3\part-00000')
# centroid_x, centroid_y = read_data('centroids.txt')
# Plotting
plt.figure(figsize=(10, 6))

# Plot data points
plt.scatter(data_x, data_y, color='blue', label='Data Points')

# Plot centroids
plt.scatter(centroid_x, centroid_y, color='red', marker='*', s=200, label='Centroids')

# Title and labels
plt.title('Data Points and Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Legend
plt.legend()

# Display the plot
plt.show()
