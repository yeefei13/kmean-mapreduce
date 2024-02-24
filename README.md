# K Mean distributed version in Hadoop

### Steps to run the experiment
1. Create docker containers:
  docker-compose up
2. transfer required files into namenode
  ./setup.sh
3. go into namenode container and setup files in hadoop hdfs
   docker exec -it namenode /bin/bash
   cd tmp
   setup-hdfs.sh
4. run k mean distributed algorithm in the same directory:
  ./run.sh

### To run different experiment
change the parameters in run.sh to experiment on different number of mapper/reducers, different memory allocated for the executors...

run.sh:
...
    hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -D mapreduce.job.reduces=1 \
    -D mapreduce.map.memory.mb=20 \
    -D mapreduce.reduce.memory.mb=20 \
    -files ./mapper.py,./reducer.py,./centroids.txt \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -input /user/root/dataset.txt \
    -output /user/root/testMapReduce/mapreduce-output$i \
...


### NOTE: in order to run python, run the following command in each container
enter container: docker exec -it namenode /bin/bash

echo "deb http://archive.debian.org/debian/ stretch main non-free contrib" > /etc/apt/sources.list
echo "deb-src http://archive.debian.org/debian/ stretch main non-free contrib" >> /etc/apt/sources.list
echo "deb http://archive.debian.org/debian-security/ stretch/updates main" >> /etc/apt/sources.list
echo "deb-src http://archive.debian.org/debian-security/ stretch/updates main" >> /etc/apt/sources.list

apt update
apt install python3
