load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

  fid2 = addfile("india.nc", "r")
  system("rm -rf test.nc")
  system("cdo remapbil,india.nc MADApdsi.nc MADApdsi_india.nc")
  fid1 = addfile("MADApdsi_india.nc", "r")
  fido = addfile("MADApdsi_india_post.nc", "c")
pdsi = fid1->PDSI
printVarSummary(pdsi)
imd = fid2->rf
;printVarSummary(imd)
;print(imd(0,1,1))

dims=dimsizes(pdsi)
;print(dims1(0))
;print(dims1(1))
;print(dims1(2))
;
;dims2=dimsizes(imd)
;print(dims2(0))
;print(dims2(1))
;print(dims2(2))
;end
;print(pdsi(0,0,0))
;if( isnan_ieee(pdsi(0,0,0))) then
;print("If logical working")
;end if
;end
;end

do k=0,dims(2)-1
do j=0,dims(1)-1
do i=0,dims(0)-1

if( (isnan_ieee(pdsi(i,j,k))).or.(ismissing(imd(0,j,k))) ) then
;print("If logical working`")
pdsi(i,j,k) = -999.0
end if

end do
end do
end do

;var1 = new((/dims(0),dims(1),dims(2)/),"float")
printVarSummary(pdsi)
pdsi@FillValue = -999.0
printVarSummary(pdsi)
varname = "pdsi"
fido->$varname$ = pdsi

end 
