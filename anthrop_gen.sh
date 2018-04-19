#!/bin/bash

lambda=(3470 2790 2320 2050 1780 1460 1270 1000 700 550 400 300 230 8000)
len=${#lambda[@]}
for (( i=0; i<${len}; i++ ));
do
   #echo ${lambda[$i]}
   for yyyy in {1850..2005}
      do
  	./exec ${lambda[$i]} $yyyy

gt_t_8000_2005.nc
      done
done
ncks -v time zorl.nc time.nc

for (( i=0; i<${len}; i++ ));
do
   #echo ${lambda[$i]}
   for yyyy in {1850..2005}
      do


   cdo remapbil,zorl.nc gt_t_${lambda[$i]}_${yyyy}.nc  aer_gt_t_${lambda[$i]}_${yyyy}.nc
   ncks -C -x -v time aer_gt_t_${lambda[$i]}_${yyyy}.nc temp.nc
   ncks -A time.nc temp.nc
   mv temp.nc aer_gt_t_${lambda[$i]}_${yyyy}.nc
done
done

./anthrop_gen_merge.sh 
