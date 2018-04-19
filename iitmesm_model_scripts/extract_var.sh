for yyyy in $@

do

list=`ls atm_mon_${yyyy}*`

echo "#!/bin/bash" > extract_var_${yyyy}.sh 

echo "set -e" >> extract_var_${yyyy}.sh

for i in $list

do
#echo "ncks -v uas,vas,tas,rlut,rsut,rsdt,rsds,rsus,rlus,rlds,hfls,hfss,prsn,pr $i var_$i" >>  extract_var_${yyyy}.sh
echo "ncks -v rsus,rsuscs,rsdt,rlut,rsds,hfss,rlus,rsut,rsdscs,rlutcs,rlds,rsutcs,rldscs,hfls,rluscs,rsdsdiff,snlhflx $i var_$i" >>  extract_var_${yyyy}.sh
done

echo "ncrcat var_atm_mon_*${yyyy}* var_merged_${yyyy}.nc" >> extract_var_${yyyy}.sh
#echo "cdo yearmean selvar_merged_${yyyy}.nc yrmean_selvar_merged_${yyyy}.nc" >> extract_var_${yyyy}.sh
#echo "rm var_atm_* -f" >> extract_var_${yyyy}.sh
echo "echo all done" >> extract_var_${yyyy}.sh

chmod +x extract_var_${yyyy}.sh
bsub -q "cccr-res" -W 240:00 -o var_atm_${yyyy}.out -e var_atm_${yyyy}.out -J var_atm_${yyyy} < ./extract_var_${yyyy}.sh

done
