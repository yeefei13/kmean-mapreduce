#!/bin/bash
i=1
hadoop fs -rm -r /user/root/testMapReduce
rm centroid-part-*
while :
do
	# hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \-files ./mapper.py,./reducer.py,./centroids.txt \-mapper "python3 mapper.py" \-reducer "python3 reducer.py" \-input /user/root/input/dataset.txt \-output /testMapReduce/mapreduce-output$i
	hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.map.memory.mb=20 \
	-D mapreduce.reduce.memory.mb=20 \
	-files ./mapper.py,./reducer.py,./centroids.txt \
	-mapper "python3 mapper.py" \
	-reducer "python3 reducer.py" \
	-input /user/root/dataset.txt \
	-output /user/root/testMapReduce/mapreduce-output$i \

	rm -f centroids1.txt
	echo $i
	# hadoop fs -cat /user/root/testMapReduce/mapreduce-output$i/part-00000

	# hadoop fs -copyToLocal /user/root/testMapReduce/mapreduce-output$i/part-00000 centroids1.txt
	
	# Specify the directory on HDFS
	hdfs_output_dir="/user/root/testMapReduce/mapreduce-output$i"
	# Specify the local directory to save files
	local_dir="."

	# List all files in the HDFS output directory
	hadoop fs -ls $hdfs_output_dir | while read line; do
	# Extract the filename from the listing
	file=`echo $line | awk '{print $8}'`
	filename=`basename $file`
	rm centroid-part-*
	# Check if filename starts with "part-" (to ignore other files like "_SUCCESS")
	if [[ $filename == part-* ]]; then
		# Construct local filename with desired naming convention
		local_filename="centroid-${filename}"
		echo "Copying $file to $local_dir/$local_filename"
		# Copy file from HDFS to local file system
		hadoop fs -copyToLocal $file $local_dir/$local_filename
		cat $local_dir/$local_filename
	fi
	done

	cat centroid-part-* > centroids1.txt
	# cat centroids1.txt
	# cat centroids.txt
	
	seeiftrue=`python3 reader.py`
	if [ $seeiftrue = 1 ]
	then
		rm centroids.txt
		cat centroids1.txt > centroids.txt
		break
	else
		rm centroids.txt
		cat centroids1.txt > centroids.txt
	fi
	i=$((i+1))
done
hadoop fs -copyToLocal /user/root/testMapReduce/ output