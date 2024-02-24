import numpy as np
import matplotlib.pyplot as plt

def generate_dataset(centroids_file, num_datapoints, sparsity):
    # Read centroids from file
    centroids = np.loadtxt(centroids_file, delimiter=',')

    dataset = []
    for centroid in centroids:
        # Generate points around each centroid based on sparsity
        num_points = num_datapoints // len(centroids)  # Equally distribute points among centroids
        points = np.random.normal(loc=centroid, scale=sparsity, size=(num_points, 2))
        dataset.extend(points)

    # Shuffle the dataset
    np.random.shuffle(dataset)

    # Trim dataset to the desired number of data points
    dataset = dataset[:num_datapoints]

    # Convert dataset to string in the specified format
    dataset_str = '\n'.join([','.join(map(str, point)) for point in dataset])
    return dataset_str
    
# Function to read data from a file
def read_data(file_path):
    x, y = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x_value, y_value = line.strip().split(',')
            x.append(float(x_value))
            y.append(float(y_value))
    return x, y

if __name__ == "__main__":
    centroids_file = "centroids.txt"
    num_datapoints = 105000  # Specify the number of data points
    sparsity = 49  # Adjust sparsity parameter as needed
    print(num_datapoints)
    dataset = generate_dataset(centroids_file, num_datapoints, sparsity)

    # Save dataset to text file
    with open("generated_dataset.txt", "w") as f:
        f.write(dataset)

    # Read data points
    data_x, data_y = read_data('generated_dataset.txt')

    # Read centroids
    centroid_x, centroid_y = read_data('centroids.txt')

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
