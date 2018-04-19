 # Start of the Makefile
 #  # Defining Variables
 # Syntax
 #  # Target: Dependencies
 #       Command
 #        #-------------------- specify netcdf library path ---------------------
 #-------------------- for IITM Aaditya HPC ----------------------------
  NETCDFINC =  -I/gpfs1/home/Libs/INTEL/NETCDF4/netcdf-4.2.1/include
  NETCDFLIB =  -L/gpfs1/home/Libs/INTEL/NETCDF4/netcdf-4.2.1/lib
 
  #----------------------------------------------------------------------
 
  LDFLAGS= $(NETCDFINC) $(NETCDFLIB) -lnetcdf -lnetcdff -g -traceback -r16 
  FC=ifort
 
 #FFLAGS=-O2 -fp-model precise -vec-report -g -traceback -mcmodel=large -heap-arrays
 
 OBJS=sp_driver_v1.o mo_simple_plumes_v1.o readfromnc.o
 
 # Makefile
  
sp_driver_v1:$(OBJS)
	$(FC) $(OBJS) $(LDFLAGS) -o exec
             
sp_driver_v1.o: sp_driver_v1.f90 mo_simple_plumes_v1.o readfromnc.o
	$(FC) -c $(NETCDFINC) sp_driver_v1.f90

mo_simple_plumes_v1.o: mo_simple_plumes_v1.f90
	$(FC) -c $(NETCDFINC) mo_simple_plumes_v1.f90

readfromnc.o: readfromnc.f90
	$(FC) -c $(NETCDFINC) readfromnc.f90

# ----- This clean is executed only when you do "make clean" -----------
# ----- If you do "make" then everything else above this "clean" -------
#   # ----- is executed ----------------------------------------------------
 
clean:
	rm -rf $(OBJS) 
	rm -rf exec
 
 # End of Makefile
  

