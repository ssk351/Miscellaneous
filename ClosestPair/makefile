# Start of the Makefile
# Defining Variables
# Syntax
# Target: Dependencies
# 	Command
#-------------------- specify netcdf library path ---------------------
#-------------------- for IITM Aaditya HPC ----------------------------

NETCDFINC =  -I/gpfs1/home/Libs/INTEL/NETCDF4/netcdf-4.2.1/include
NETCDFLIB =  -L/gpfs1/home/Libs/INTEL/NETCDF4/netcdf-4.2.1/lib

#----------------------------------------------------------------------
CFLAGS = -O3 -C  -axAVX -align array32byte #-ipo

LDFLAGS = $(CFLAGS) -L/gpfs7/home/ibm/AMIT/FFTW/fftw-3.2.2/FFTW/lib -lfftw3 -L/gpfs1/home/Libs/INTEL/SIONLIB/sionlib-1.5.5/lib -lsionmpi_cxx_64 -lsionmpi_f77_64 -lsionmpi_f90_64 -lsionser_f90_64 -lsionmpi_64 -lsionser_64 -lsioncom_64 -lsioncom_64_lock_none -lsionser_f77_64

FC=mpiifort
FFLAGS= -mcmodel medium -shared-intel -g -traceback

OBJS = testing_random_3d.o closest_pair_module_3d.o

# Makefile

main_program_3:$(OBJS)
	$(FC) $(OBJS) $(LDFLAGS) -o exe

testing_random_3d.o : testing_random_3d.f90 closest_pair_module_3d.o
	$(FC) -c $(FFLAGS) testing_random_3d.f90

closest_pair_module_3d.o: closest_pair_module_3d.f90
	$(FC) -c $(FFLAGS) closest_pair_module_3d.f90

# ----- This clean is executed only when you do "make clean" -----------
# ----- If you do "make" then everything else above this "clean" -------
# ----- is executed ----------------------------------------------------

clean :
	rm -rf $(OBJS) 
	rm -rf exe *.mod *.o

# End of Makefile


