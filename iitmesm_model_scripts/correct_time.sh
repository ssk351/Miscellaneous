#!/bin/bash

for yyyy in {1850..1850}
do

echo "netcdf time_anthrop_${yyyy} {" > time_${yyyy}.txt
echo "dimensions:" >> time_${yyyy}.txt
echo "	time = UNLIMITED ; // (12 currently)" >> time_${yyyy}.txt
echo "variables:" >> time_${yyyy}.txt
echo "	double time(time) ;" >> time_${yyyy}.txt
echo "		time:standard_name = \"time\" ;" >> time_${yyyy}.txt
echo "		time:long_name = \"initial time\" ;" >> time_${yyyy}.txt
echo "		time:units = \"day as %Y%m%d.%f\" ;" >> time_${yyyy}.txt
echo "		time:calendar = \"standard\" ;" >> time_${yyyy}.txt
echo "data:" >> time_${yyyy}.txt
echo " " >> time_${yyyy}.txt
echo " time = ${yyyy}0101, ${yyyy}0201, ${yyyy}0301, ${yyyy}0401, ${yyyy}0501, ${yyyy}0601, ${yyyy}0701, " >> time_${yyyy}.txt
echo "    ${yyyy}0801, ${yyyy}0901, ${yyyy}1001, ${yyyy}1101, ${yyyy}1201 ; " >> time_${yyyy}.txt
echo "}" >>time_${yyyy}.txt

done

for yyyy in {1850..1850}
do

ncgen -o time_${yyyy}.nc time_${yyyy}.txt 
ncks -C -x -v time anthrop_${yyyy}.nc temp.nc
ncks -A time_${yyyy}.nc temp.nc
mv temp.nc anthrop_iitmesm_${yyyy}.nc

done
