load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl" 
; Run Example
; ncl 'fili = "atm_day_2446.nc"' analysis.ncl
; Input file: any time merged file
;fili = "atm_day_2446.nc"
fid = addfile(fili, "r")
;fido = addfile("test.nc", "c")
rsdt = fid->rsdt
rsut = fid->rsut
rlut = fid->rlut
rsds = fid->rsds
rlds = fid->rlds
rsus = fid->rsus
rlus = fid->rlus
hfss = fid->hfss
hfls = fid->hfls
pr = fid->pr 
ts = fid->ts

lat = fid->lat
toa = rsdt - rsut - rlut
sfc = rsds + rlds - rsus - rlus - hfss - hfls
rad    = 4.0*atan(1.0)/180.0
clat   = cos(lat*rad)

toa_ave = wgt_areaave(toa,clat,1.0,1)
sfc_ave = wgt_areaave(sfc,clat,1.0,1)
pr_ave = wgt_areaave(pr,clat,1.0,1)
ts_ave = wgt_areaave(ts,clat,1.0,1)-273.15

print("TOA flux = "+dim_avg(toa_ave))
print("SFC flux = "+dim_avg(sfc_ave))
print("PR = "+dim_avg(pr_ave))
print("TS = "+dim_avg(ts_ave))
