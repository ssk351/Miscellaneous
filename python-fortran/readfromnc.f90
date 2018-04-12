subroutine readfromnc(FILE_NAME, var_NAME, readvar, lons, lats, lvls, recs, NLONS, NLATS, NLVLS, NRECS)
  use netcdf
  implicit none
  
  character (len = *) :: var_NAME
  character (len = *):: FILE_NAME 
  integer :: ncid

  integer, parameter :: NDIMS = 4
  integer            :: NLVLS , NLATS , NLONS , NRECS
  character (len = *), parameter :: LVL_NAME = "level"
  character (len = *), parameter :: LAT_NAME = "latitude"
  character (len = *), parameter :: LON_NAME = "longitude"
  character (len = *), parameter :: REC_NAME = "time"
  integer :: lvl_dimid, lon_dimid, lat_dimid, rec_dimid

  integer :: start(NDIMS), count(NDIMS)

  real :: lats(NLATS), lons(NLONS), lvls(NLVLS), recs(NRECS)
  integer :: lon_varid, lat_varid, lvl_varid, rec_varid

  integer :: var_varid
  integer :: dimids(NDIMS)

  character (len = *), parameter :: UNITS = "units"
  character (len = *), parameter :: var_UNITS = "hPa"
  character (len = *), parameter :: LAT_UNITS = "degrees_north"
  character (len = *), parameter :: LON_UNITS = "degrees_east"

  real,dimension(NLONS,NLATS,NLVLS,NRECS) :: readvar
  real :: var_in(NLONS, NLATS, NLVLS)

  integer :: lvl, lat, lon, rec, i, j, k

  call check( nf90_open(FILE_NAME, nf90_nowrite, ncid) )

  call check( nf90_inq_varid(ncid, LAT_NAME, lat_varid) )
  call check( nf90_inq_varid(ncid, LON_NAME, lon_varid) )
  call check( nf90_inq_varid(ncid, LVL_NAME, lvl_varid) )
  call check( nf90_inq_varid(ncid, REC_NAME, rec_varid) )

  call check( nf90_get_var(ncid, lat_varid, lats) )
  call check( nf90_get_var(ncid, lon_varid, lons) )
  call check( nf90_get_var(ncid, lvl_varid, lvls) )
  call check( nf90_get_var(ncid, rec_varid, recs) )
  call check( nf90_inq_varid(ncid, var_NAME, var_varid) )

  count = (/ NLONS, NLATS, NLVLS, 1 /)
  start = (/ 1, 1, 1, 1 /)

  do rec = 1, NRECS
     start(4) = rec
     call check( nf90_get_var(ncid, var_varid, var_in, start = start, &
                              count = count) )
                     do k=1,NLVLS
                        do j=1,NLATS
                           do i=1,NLONS
                                readvar(i,j,k,rec)=var_in(i,j,k)
                           end do
                        end do     
                      end do
  end do
         
  call check( nf90_close(ncid) )

  print *,"*** SUCCESS reading example file ", FILE_NAME, "!"

end subroutine readfromnc

