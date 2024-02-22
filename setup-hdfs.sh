#!/bin/bash

hadoop fs -mkdir -p /user/root

hadoop fs -put sample_input.txt /user/root

hadoop fs -put dataset.txt /user/root