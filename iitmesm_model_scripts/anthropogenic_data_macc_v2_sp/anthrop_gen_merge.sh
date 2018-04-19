#!/bin/bash

lambda=(3470 2790 2320 2050 1780 1460 1270 1000 700 550 400 300 230 8000)
len=${#lambda[@]}

for (( i=0; i<${len}; i++ ));
do
for yyyy in {2005..2005} 

do
echo anthrop_${lambda[$i]}_${yyyy}_1.nc
ncks -v aod,ssa,asy aer_gt_t_${lambda[$i]}_${yyyy}.nc anthrop_${lambda[$i]}_${yyyy}_1.nc
ncrename -v aod,aod_band$i -v ssa,ssa_band$i -v asy,asy_band$i anthrop_${lambda[$i]}_${yyyy}_1.nc
ncks -A anthrop_${lambda[$i]}_${yyyy}_1.nc anthrop_${yyyy}.nc 
done

done

 
