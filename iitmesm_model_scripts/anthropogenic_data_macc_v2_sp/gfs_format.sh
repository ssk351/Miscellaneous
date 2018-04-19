#!/bin/bash
ncks -v time zorl.nc time.nc

for file in gt_t*2005.nc
do
   cdo remapbil,zorl.nc -selname,aod $file aod_$file
   cdo remapbil,zorl.nc -selname,ssa $file ssa_$file
   cdo remapbil,zorl.nc -selname,asy $file asy_$file
   ncks -C -x -v time aod_$file temp.nc
   ncks -A time.nc temp.nc
   mv temp.nc aod_$file
   ncks -C -x -v time ssa_$file temp.nc
   ncks -A time.nc temp.nc
   mv temp.nc ssa_$file
   ncks -C -x -v time asy_$file temp.nc
   ncks -A time.nc temp.nc
   mv temp.nc asy_$file
done 
