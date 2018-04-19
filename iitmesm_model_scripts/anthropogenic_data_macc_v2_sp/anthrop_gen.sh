#!/bin/bash

lambda=(3470 2790 2320 2050 1780 1460 1270 1000 700 550 400 300 230 8000)
len=${#lambda[@]}
for (( i=0; i<${len}; i++ ));
do
   #echo ${lambda[$i]}
   for yyyy in {2005..2005}
      do
  	./exec ${lambda[$i]} $yyyy
      done
done
ncks -v time zorl.nc time.nc

for file in *2005.nc
do
   cdo remapbil,zorl.nc $file aer_$file
   ncks -C -x -v time aer_$file temp.nc
   ncks -A time.nc temp.nc
   mv temp.nc aer_$file
done 
