load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

;fili_prefix = "3B42RT"
diri   = "./"                             ; input directory
fili   = systemfunc("cd "+diri+" ; ls *HDF") 
nfili  = dimsizes(fili)
print(fili)

do nf=0,nfili-1

fid = addfile(fili(nf), "r")
fido = addfile(fili(nf)+".nc", "c")
nlon = 9247
nlat = 49
nlev = 80

lat = fid->Latitude
lon = fid->Longitude
rain = fid->rain
z = fid->correctZFactor

;printVarSummary(z)

var1 = "rain"
var2 = "z"
var3 = "lon"
var4 = "lat"


fido->$var1$ = rain
fido->$var2$ = z
fido->$var3$ = lon
fido->$var4$ = lat

delete(lat)
delete(lon)
delete(rain)
delete(z)

end do

end
