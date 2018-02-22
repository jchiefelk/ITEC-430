#!/bin/bash


array=($1 $2 $3 $4 $5)

for x in "${array[@]}"
do
	echo $x
done
