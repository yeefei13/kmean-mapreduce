# K Mean distributed version in Hadoop

## Steps to run K mean in docker using hadoop
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




p.s. in order to run python, run the following command in each container
enter container: docker exec -it namenode /bin/bash

echo "deb http://archive.debian.org/debian/ stretch main non-free contrib" > /etc/apt/sources.list
echo "deb-src http://archive.debian.org/debian/ stretch main non-free contrib" >> /etc/apt/sources.list
echo "deb http://archive.debian.org/debian-security/ stretch/updates main" >> /etc/apt/sources.list
echo "deb-src http://archive.debian.org/debian-security/ stretch/updates main" >> /etc/apt/sources.list

apt update
apt install python3
