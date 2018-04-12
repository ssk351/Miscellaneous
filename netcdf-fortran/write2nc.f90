subroutine writef2nc(FILE_NAME,var_NAME, outvar, lons, lats, lvls, recs, NLONS,NLATS,NLVLS,NRECS)
  use netcdf
  implicit none

  character (len = *) :: FILE_NAME 
  integer :: ncid

  integer, parameter :: NDIMS = 4
  integer :: NLVLS , NLATS , NLONS , NRECS 
  character (len = *), parameter :: LVL_NAME = "level"
  character (len = *), parameter :: LAT_NAME = "latitude"
  character (len = *), parameter :: LON_NAME = "longitude"
  character (len = *), parameter :: REC_NAME = "time"
  integer :: lvl_dimid, lon_dimid, lat_dimid, rec_dimid

  integer :: start(NDIMS), count(NDIMS)

  real :: lats(NLATS), lons(NLONS), lvls(NLVLS), RECS(NRECS)
  integer :: lon_varid, lat_varid, rec_varid, lvl_varid
  real,dimension(NLONS,NLATS,NLVLS,NRECS) :: outvar
  character (len = *) :: var_NAME
  integer :: var_varid
  integer :: dimids(NDIMS)

  character (len = *), parameter :: UNITS = "units"
  character (len = *), parameter :: var_UNITS = "m"
  character (len = *), parameter :: LAT_UNITS = "degrees_north"
  character (len = *), parameter :: LON_UNITS = "degrees_east"
  character (len = *), parameter :: LVL_UNITS = "km"
  character (len = *), parameter :: REC_UNITS = "days since 0001-01-01 00:00:00"
  character (len = *), parameter :: REC_CALENDAR = "standard"
  character (len = *), parameter :: REC_LONGNAME = "Year AD"
  character (len = *), parameter :: REC_STANDARDNAME = "time"

  character (len = *), parameter :: LAT_STANDARDNAME = "latitude"
  character (len = *), parameter :: LAT_LONGNAME = "latitude"
  character (len = *), parameter :: LAT_AXIS = "Y"

  character (len = *), parameter :: LON_STANDARDNAME = "longitude"
  character (len = *), parameter :: LON_LONGNAME = "longitude"
  character (len = *), parameter :: LON_AXIS = "X"
  
  character (len = *), parameter :: LVL_STANDARDNAME = "level"
  character (len = *), parameter :: LVL_LONGNAME = "level"
  character (len = *), parameter :: LVL_AXIS = "Z"

  character (len = *), parameter :: VAR_SHORTNAME = "Geopotential Height"
  real,                parameter :: VAR_FillValue = -999.9
  character (len = *), parameter :: VAR_LONGNAME = "hght"

  real :: var_out(NLONS, NLATS, NLVLS)

  integer :: lvl, lat, lon, rec, i, j, k
  print *,"readvar(1,1,1,1) = ", outvar(1,1,1,1)
  call check( nf90_create(FILE_NAME, nf90_clobber, ncid) )
  
  call check( nf90_def_dim(ncid, LVL_NAME, NLVLS, lvl_dimid) )
  call check( nf90_def_dim(ncid, LAT_NAME, NLATS, lat_dimid) )
  call check( nf90_def_dim(ncid, LON_NAME, NLONS, lon_dimid) )
  call check( nf90_def_dim(ncid, REC_NAME, NF90_UNLIMITED, rec_dimid) )

  call check( nf90_def_var(ncid, LAT_NAME, NF90_REAL, lat_dimid, lat_varid) )
  call check( nf90_def_var(ncid, LON_NAME, NF90_REAL, lon_dimid, lon_varid) )
  call check( nf90_def_var(ncid, LVL_NAME, NF90_REAL, lvl_dimid, lvl_varid) )
  call check( nf90_def_var(ncid, REC_NAME, NF90_REAL, rec_dimid, rec_varid) )

  call check( nf90_put_att(ncid, lat_varid, UNITS, LAT_UNITS) )
  call check( nf90_put_att(ncid, lat_varid, "standard_name", LAT_STANDARDNAME) )
  call check( nf90_put_att(ncid, lat_varid, "long_name", LAT_LONGNAME) )
  call check( nf90_put_att(ncid, lat_varid, "axis", LAT_AXIS) )
  
  call check( nf90_put_att(ncid, lon_varid, UNITS, LON_UNITS) )
  call check( nf90_put_att(ncid, lon_varid, "standard_name", LON_STANDARDNAME) )
  call check( nf90_put_att(ncid, lon_varid, "long_name", LON_LONGNAME) )
  call check( nf90_put_att(ncid, lon_varid, "axis", LON_AXIS) )

  call check( nf90_put_att(ncid, lvl_varid, UNITS, LVL_UNITS) )
  call check( nf90_put_att(ncid, lvl_varid, "standard_name", LVL_STANDARDNAME) )
  call check( nf90_put_att(ncid, lvl_varid, "long_name", LVL_LONGNAME) )
  call check( nf90_put_att(ncid, lvl_varid, "axis", LVL_AXIS) )

  call check( nf90_put_att(ncid, rec_varid, UNITS, REC_UNITS) )
  call check( nf90_put_att(ncid, rec_varid, "standard_name", REC_STANDARDNAME) )
  call check( nf90_put_att(ncid, rec_varid, "long_name", REC_LONGNAME) )
  call check( nf90_put_att(ncid, rec_varid, "calendar", REC_CALENDAR) )


  dimids = (/ lon_dimid, lat_dimid, lvl_dimid, rec_dimid /)

  call check( nf90_def_var(ncid, var_NAME, NF90_REAL, dimids, var_varid) )

  call check( nf90_put_att(ncid, var_varid, UNITS, VAR_UNITS) )
  call check( nf90_put_att(ncid, var_varid, "_FillValue", VAR_FillValue) )
  call check( nf90_put_att(ncid, var_varid, "long_name", VAR_LONGNAME) )
  call check( nf90_put_att(ncid, var_varid, "short_name", VAR_SHORTNAME) )

 
  ! End define mode.
  call check( nf90_enddef(ncid) )

  call check( nf90_put_var(ncid, lat_varid, lats) )
  call check( nf90_put_var(ncid, lon_varid, lons) )
  call check( nf90_put_var(ncid, lvl_varid, lvls) )
  call check( nf90_put_var(ncid, rec_varid, recs) )
  
  count = (/ NLONS, NLATS, NLVLS, 1 /)
  start = (/ 1, 1, 1, 1 /)

  do rec = 1, NRECS
     start(4) = rec
     call check( nf90_put_var(ncid, var_varid, outvar(:,:,:,rec), start = start,  count = count) )

!                do k=1,NLVLS
!                        do j=1,NLATS
!                           do i=1,NLONS
!                                outvar(i,j,k,rec)=var_out(i,j,k)
!         
!                           end do
!                        end do     
!                end do
!     outvar(:,:,:,rec) = var_out(:,:,:)
  end do
  
  call check( nf90_close(ncid) )
  
  print *,"*** SUCCESS writing example file ", FILE_NAME, "!"

end subroutine writef2nc
  subroutine check(status)
    integer, intent ( in) :: status
    
    if(status /= nf90_noerr) then 
      !print *, trim(nf90_strerror(status))
      stop "Stopped"
    end if
  end subroutine check  

