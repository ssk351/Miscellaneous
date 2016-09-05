load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

  nlon = 192
  nlat = 94
  nband = 14
  nlev = 70

  fid = addfile("cmip6_data/ext_omega_g_sun.nc", "r")
  fid1 = addfile("zorl.nc", "r")
  system("rm -rf strato_aod_1850.nc")
  fido = addfile("strato_aod_1850.nc", "c")

  lon = fid1->lon
  
  print(fid)

  

  do i = 0, 13
    
    var = fid->ext_sun_new1(month|0:11,altitude|:,solar_bands|i,lat|:)
    dims=dimsizes(var)
    var1 = new((/dims(0),dims(1),dims(2),192/),"float")
    
    do j =0, nlon-1 
      var1(:,:,:,j) = var(:,:,:)
    end do
    var1!3="lon"
    var1&lon=lon
    
    n=i+1
    bnd="band"+n
    fido->$bnd$ = var1

    delete(var)
    delete(

    var1)
    
  end do
  
  ;printVarSummary(var)
  
end
