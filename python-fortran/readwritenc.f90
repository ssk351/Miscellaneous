program var_temp_4D_wr

integer, parameter :: NLVLS = 64, NLATS = 94, NLONS = 192, NRECS = 12
real,dimension(NLONS,NLATS,NLVLS,NRECS) :: outvar, readvar
character (len = *), parameter :: FILE_NAME = "allforcing_present_day_mh.nc"
character (len = *), parameter :: var_NAME="height"
real :: lats(NLATS), lons(NLONS), lvls(NLVLS), recs(NRECS)

call readfromnc(FILE_NAME,var_NAME, readvar,lons, lats, lvls, recs, NLONS, NLATS, NLVLS, NRECS)
print *,"readvar(1,1,1,1) = ",readvar(1,1,1,1)
call writef2nc("test.nc", "test_var", readvar, lons, lats, lvls, recs, NLONS, NLATS, NLVLS, NRECS)
print *,"readvar(1,1,1,1) = ",readvar(1,1,1,1)
!print *,"lvl from write2nc = ",lvls
!print *,"lat from writef2nc = ",lats, "lons from writef2nc = ",lons

end program var_temp_4D_wr


