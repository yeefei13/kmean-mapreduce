#!/bin/bash
i=1
while :
do
	# hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \-files ./mapper.py,./reducer.py,./centroids.txt \-mapper "python3 mapper.py" \-reducer "python3 reducer.py" \-input /user/root/input/dataset.txt \-output /testMapReduce/mapreduce-output$i
	hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
	-files ./mapper.py,./reducer.py,./centroids.txt \
	-mapper "python3 mapper.py" \
	-reducer "python3 reducer.py" \
	-input /user/root/sample_input.txt \
	-output /user/root/testMapReduce/mapreduce-output$i

	rm -f centroids1.txt
	echo $i
	hadoop fs -cat /user/root/testMapReduce/mapreduce-output$i/part-00000

	hadoop fs -copyToLocal /user/root/testMapReduce/mapreduce-output$i/part-00000 centroids1.txt
	seeiftrue=`python3 reader.py`
	if [ $seeiftrue = 1 ]
	then
		rm centroids.txt
		hadoop fs -copyToLocal /user/root/testMapReduce/mapreduce-output$i/part-00000 centroids.txt
		break
	else
		rm centroids.txt
		hadoop fs -copyToLocal /user/root/testMapReduce/mapreduce-output$i/part-00000 centroids.txt
	fi
	i=$((i+1))
done
hadoop fs -copyToLocal /user/root/testMapReduce/ output