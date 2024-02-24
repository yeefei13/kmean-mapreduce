from mapper import getCentroids
from itertools import product

# Function to check if the distance between any pair of centroids is less than 1
def checkCentroidsDistance(centroids, centroids1):
    # Iterate over all possible pairs of centroids
    for c1, c2 in product(centroids, centroids1):
        # Calculate the difference in x and y coordinates
        dx = abs(c1[0] - c2[0])
        dy = abs(c1[1] - c2[1])
        
        # Check if both differences are less than 1
        if dx < 1 and dy < 1:
            print(1)
            return
    # If no pair is close enough, print 0
    print(0)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)
