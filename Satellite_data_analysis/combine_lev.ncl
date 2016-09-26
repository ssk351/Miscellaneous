load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

fid = addfile("TrmmBin_bin_sum.nc", "r")

fido = addfile("TrmmBin_bin_lev.nc", "c")
  nlat  = 480                       ; grid coordinates
  mlon  = 1440
  nlev  = 80
var1 = new((/nlat,mlon,1,nlev/),float)
var2 = new((/1,nlev,nlat,mlon/),float)
lev = new((/nlev/),float)
  do k=0,nlev-1
    lev(k) = 0.25*(k+1)
  end do

  lev!0 = "lev"
  lev@units = "km from MSL"
	var1!3 = "lev"
	var1&lev = lev
	var1!2 = "time"
	
lev = new((/nlev/),float)
	do k=1,nlev-1
		vNam  = "correctZFactor"
		vNam = vNam + k
		var = fid->$vNam$
		var1(:,:,:,k) =var(:,:,:)
	end do
var2 = var1(time|:,lev|:,lat|:,lon|:)
vNam  = "correctZFactor"
fido->$vNam$ = var2
;printVarSummary(var1)

delete(var)
delete(var1)

end
