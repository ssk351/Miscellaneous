for file in aer_gt_t_*_2005.nc
do
   cdo selname,aod $file aod_$file
   cdo selname,ssa $file ssa_$file
   cdo selname,asy $file asy_$file
done

