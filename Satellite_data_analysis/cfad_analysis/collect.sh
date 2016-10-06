#!/bin/bash

for year in {2005..2014}
do 
for mm in {06..09}
do
	tmpfile=$(mktemp --suffix=".sh")
	echo "cp ${year}/${mm}/* 2005_14/" >> $tmpfile
	bsub -q "cccr-res" -W 10:00 -J "swath_${file}" -o "collect.out" < $tmpfile 
done

done
