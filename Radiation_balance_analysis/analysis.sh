#!/bin/bash

if [ ${#@} == 0 ]; then
    echo "Usage: $0 aero noaero"
    echo "* aero:   <file containing aero catted time series file>"
    echo "* noaero: <file containing noaero catted time series file>"
fi

cp $1 aer.nc
cp $2 noaer.nc

ncks -v pr,ts,rsdt,rsut,rlut,rsds,rlds,rsus,rlus,hfss,hfls aer.nc ext_aer.nc
ncks -v pr,ts,rsdt,rsut,rlut,rsds,rlds,rsus,rlus,hfss,hfls noaer.nc ext_noaer.nc

cdo selmon,6/9 ext_aer.nc ext_aer_jjas.nc
cdo selmon,6/9 ext_noaer.nc ext_noaer_jjas.nc

cdo timmean ext_aer_jjas.nc aer_jjas.nc
cdo timmean ext_noaer_jjas.nc noaer_jjas.nc

cdo timmean ext_aer.nc aer_ann.nc
cdo timmean ext_noaer.nc noaer_ann.nc

ncdiff aer_ann.nc noaer_ann.nc aer-noaer_ann.nc
ncdiff aer_jjas.nc noaer_jjas.nc aer-noaer_jjas.nc

ncl 'fili = "aer.nc"' analysis.ncl
ncl 'fili = "noaer.nc"' analysis.ncl

mkdir ann jjas
ferret -gif -script analysis.jnl aer-noaer_ann.nc
mv *.gif ann/

ferret -gif -script analysis.jnl aer-noaer_jjas.nc
mv *.gif jjas/
