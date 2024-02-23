#!/bin/bash

# Copy centroids.txt to namenode:/tmp
docker cp centroids.txt namenode:/tmp

# Copy mapper.py to namenode:/tmp
docker cp mapper.py namenode:/tmp

# Copy reducer.py to namenode:/tmp
docker cp reducer.py namenode:/tmp

# Copy dataset.txt to namenode:/tmp
docker cp dataset.txt namenode:/tmp

# Copy run.sh to namenode:/tmp
docker cp run.sh namenode:/tmp

# Copy reader.py to namenode:/tmp
docker cp reader.py namenode:/tmp

# Copy reader.py to namenode:/tmp
docker cp sample_input.txt namenode:/tmp

# Copy reader.py to namenode:/tmp
docker cp setup-hdfs.sh namenode:/tmp