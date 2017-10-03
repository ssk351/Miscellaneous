import sys, string
from matplotlib import rc
import numpy
import pylab as pl
import netCDF4
import time as t
import datetime
from dateutil.parser import parse
from pylab import load, meshgrid, title, arange, show
from netcdftime import utime
import scipy.io
import matplotlib as mpl
import argparse
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import datetime as dt

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#map = Basemap(projection='ortho', lat_0=0, lon_0=0)
#map = Basemap(projection='cyl')
map = Basemap(llcrnrlon=60.0,llcrnrlat=5.0,urcrnrlon=100.0,urcrnrlat=40.0, resolution = 'h', epsg=5520)

#Fill the globe with a blue color 
map.drawmapboundary(fill_color='aqua')
#Fill the continents with the land color
map.fillcontinents(color='coral',lake_color='aqua')

map.drawcoastlines()

pl.show()
#Plotting directly from netcdf file in python
#from osgeo import gdal
#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt
#
#wrf_out_file = "wrfout_v2_Lambert.nc"
#
#ds_lon = gdal.Open('NETCDF:"'+wrf_out_file+'":XLONG')
#ds_lat = gdal.Open('NETCDF:"'+wrf_out_file+'":XLAT')
#
#ds_t2 = gdal.Open('NETCDF:"'+wrf_out_file+'":T2')
#
#map = Basemap(llcrnrlon=-95.,llcrnrlat=27.,urcrnrlon=-65.,urcrnrlat=40.,
#              projection='lcc', lat_1=30.,lat_2=60.,lat_0=34.83158,lon_0=-98.)
#
#x, y = map(ds_lon.ReadAsArray()[1], ds_lat.ReadAsArray()[1])
#
#map.contourf(x, y, ds_t2.ReadAsArray()[1]) 
#
#map.drawcoastlines()
#plt.show()
#Subplot
#https://basemaptutorial.readthedocs.io/en/latest/subplots.html
#Plotting data in python
#https://basemaptutorial.readthedocs.io/en/latest/plotting_data.html

#Basemap arguments
#https://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.interp
#llcrnrlon	longitude of lower left hand corner of the desired map domain (degrees).
#llcrnrlat	latitude of lower left hand corner of the desired map domain (degrees).
#urcrnrlon	longitude of upper right hand corner of the desired map domain (degrees).
#urcrnrlat	latitude of upper right hand corner of the desired map domain (degrees).
