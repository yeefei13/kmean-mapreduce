#!/usr/bin/env python

import sys
from math import sqrt
import logging
# Basic configuration for logging
# logging.basicConfig(level=logging.DEBUG, # Minimum level of messages to log
#                     format='%(asctime)s - %(levelname)s - %(message)s', # Format of log messages
#                     filename='mapper.log', # File to write log messages to
#                     filemode='w') # Mode for the log file ('w' for overwrite; 'a' for append)

# # Create a logger object
# logger = logging.getLogger()

# Get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    centroids = []

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    cord = line.split(', ')
                    # cord[0] is x and cord[1] is y point of a centroid
                    centroids.append([float(cord[0]), float(cord[1])])
                except:
                    # logger.error("strip failed")
                    break
            else:
                break
            line = fp.readline()
    return centroids

# Create clusters based on initial centroids
def createClusters(centroids):
    for line in sys.stdin:
        line = line.strip()
        cord = line.split(',')
        min_dist = 100000000000000
        index = -1
        for centroid in centroids:
            try:
                cord[0] = float(cord[0])
                cord[1] = float(cord[1])
            except ValueError:
                # Float was not a number, so silently
                # ignore/discard this line
                continue

            # Euclidean distance from every point of dataset
            # to every centroid
            cur_dist = sqrt(pow(cord[0] - centroid[0], 2) + pow(cord[1] - centroid[1], 2))

            # Find the centroid which is closer to the point
            if cur_dist <= min_dist:
                min_dist = cur_dist
                index = centroids.index(centroid)
        # logger.info(f'point {cord} is assigned to centroid {index}')
        var = "%s\t%s\t%s" % (index, cord[0], cord[1])
        print(var)


if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    createClusters(centroids)
