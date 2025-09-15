"""
GeoData Science with Python, S. Werth
Code snippets for plotting NetCDF data

Created on Mon Oct 12 18:54:30 2021
@author: swerth
"""
import matplotlib.pyplot as plt
import numpy as np
import netCDF4
from netCDF4 import Dataset
from netCDF4 import date2index
from datetime import datetime


# Open netcdf dataset
# --------------------------------
data = Dataset('gistemp250_GHCNv4.nc')


# read data - COMPLETE THIS PART
# --------------------------------

# Get index for location of a certain date (month) in the time vector
year = 2021
month = 1
timeindex = date2index(datetime(year, month, 15),
                       data.variables['time'])



# complete the code here:
###  read lat, lon, time and anomaly into numpy arrays

###  read tempanomaly for month defined by 'timeindex' above

###  replace fill values

###  close the file




# plot data 
# --------

# converting the 1D coordinate arrays to a meshgrid
lonGrid, latGrid = np.meshgrid(lon,lat)

# plot data into map
fig = plt.figure(figsize=(8, 4))

# plotting the first last map in the time series
plt.pcolormesh(lonGrid,latGrid, anom, shading='auto',cmap='nipy_spectral') 
# try other colorbars: hot, hot_r, cool

# adding a colorbar and title
plt.title('Temperature Anomaly ' + str(datetime(year, month, 15)))
plt.colorbar(label=('temperature anomaly (' + u'\N{DEGREE SIGN}' + 'C)'))

# add plot limits
#plt.clim(-8, 8)

# read out available time period from netcdf file, store in string, 
# and write to plot
t_units = data.variables['time'].units
time_beg = netCDF4.num2date(data.variables['time'][0],t_units)
time_end = netCDF4.num2date(data.variables['time'][-1],t_units)
print('\nThis netcdf file contains records from ' + str(time_beg) +
      ' to ' + str(time_end))


