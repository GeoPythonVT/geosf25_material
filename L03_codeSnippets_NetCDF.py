"""
GeoData Science with Python, S. Werth
Code snippets for working with NetCDF

Created on Sun Sep 14 2025
@author: swerth
"""
   
    
# ------------------------------------------
# CODE 1 - Download a file with Requests
# ------------------------------------------

# 1. Import the requests module
import requests

# 2. Define the URL for the file to download
filename = 'gistemp250_GHCNv4.nc.gz'
url = 'https://data.giss.nasa.gov/pub/gistemp/' + filename

# 3. Use requests.get() to download the data behind that URL
response = requests.get(URL)

# 4. Write the file to a new file
f=open(filename, "wb")
f.write(response.content)
f.close()



# ------------------------------------------
# CODE 2 - Download a file with urllib
# ------------------------------------------

# 1. Import the urllib module
import urllib

# 2. Define the URL for the file to download
#    here: VT logo
filename = 'gistemp250_GHCNv4.nc.gz'
url = 'https://data.giss.nasa.gov/pub/gistemp/' + filename

# 3. urllib‘s request.urlretrieve() method to
#    download a file from a specific URL 
#    and save it to a new file called
#    "VTlogo.svg"
response = urllib.request.urlretrieve(url, filename)



# ------------------------------------------
# CODE 3 - Unzip a file (only relevant if file is zipped)
# ------------------------------------------

# Unzip the file: bash command in a notebook cell
!gunzip -f -k {filename} # unpacks the file, 
                         # -f forces command & overwrites files
                         # -k keeps both files .gz and unzipped one
# Information on gunzip: https://www.tutorialspoint.com/unix_commands/gunzip.htm


# alternative way to unzip the file via Python module gzip
# import gzip
# import shutil
# filename_unzip = filename.replace('.gz', '')
# with gzip.open(filename, 'rb') as f_in:
#     with open(filename_unzip, 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)




# ------------------------------------------
# CODE 4 - Working with NetCDF4
# ------------------------------------------

# Import the self-describing data
# ------------------------------------------

# Check, if installation of netCDF4 is available
from netCDF4 import Dataset
# switch environtment if needed!

# Import the dataset
filename = 'gistemp250_GHCNv4.nc'
data = Dataset(filename, mode='r')

# closing the netCDF file
#data.close()



# Tutorial 1: Explore the self-describing data
# ------------------------------------------

data.variables # call attribute `variables`
data.dimensions # call attibute `dimensions`



# Tutorial 2: Info for variable and dimension
# ------------------------------------------

# Retrieve list of available variables in data
print ([e for e in data.variables])

# Retrieve list of available dimension names 
print ([e for e in data.dimensions])

# Retrieve list of available dimension values
print ([data.dimensions[e].size for e in data.dimensions])



# Tutorial 3: Info for individual variables
# ------------------------------------------

# Receive info on variable ...
data.variables['lat'] # 'lat'
data.variables['lon'] # 'lon'
data.variables['tempanomaly'] # 'tempanomaly'

# Receive content of attributes of variable 'tempanomaly'
data.variables['tempanomaly'].long_name
data.variables['tempanomaly'].units
data.variables['tempanomaly']._FillValue



# Tutorial 4: Variable content
# ------------------------------------------

# retrieves masked array:
data.variables['tempanomaly'][:]
data.variables['lon'][:]
# mask only present for some netcdf variables
# here: for lat, lon, mask is empty

# Check if variable lon contains a mask container (true)
data.variables['lon'].mask

# Check if the mask container is filled (false)
data.variables['lon'][:].mask



# Tutorial 5: Variable values
# ------------------------------------------

# reference the first entry in data array
data.variables['lon'][0].data

# reference all entries in the data array:
lon = data.variables['lon'][:].data

# writing content of a variable (data and mask) into new variable
anom = data.variables['tempanomaly'][:].data
mask = data.variables['tempanomaly'][:].mask

# Check shape and dtype of the new variables 
# (these are numpy arrays!)
import numpy # need to import numpy now
lon.shape, lat.shape, time.shape, anom.shape, mask.shape
lon.dtype, lat.dtype, time.dtype, anom.dtype, mask.dtype



# Tutorial 6: Working with netCDF4 time values
# ------------------------------------------
# Netcdf time vectors are stored as running integer, and a unit attribute providing information for convertion to dates

# Recive unit of the time vector in data
data.variables['time'].units

# store units of the netCDF time vector in variable
unts = data.variables['time'].units

# import the netcdf num2date to convert time values 
from netCDF4 import num2date
# convert the netcdf time values to a date with num2date
time_dates = num2date(time,unts)  # string: 'days since 1800-01-01 00:00:00'

# date is given in netCDF's cftimec class:
type(time_dates[0])

# receive date as string with cftime method strftime
time_dates[1].strftime()
#str(time_dates[1])   # alternatively


# convert cftime dates to netcdf time values with date2num
from netCDF4 import date2num
date2num(time_dates,unts)

# convert datetime dates to netcdf time values with date2num
from datetime import datetime
date2num(datetime(2021, 9, 15),unts)

# convert datetime date to an index corresponding to netcdf time unit
from netCDF4 import date2index
from datetime import datetime
timeindex = date2index(datetime(2021, 1, 15),data.variables['time'])

# or use cftime
import cftime
timeindex_cf = date2index(cftime.DatetimeGregorian(2021, 1, 15),data.variables['time'])




# Tutorial 7: Plotting netCDF4 data
# ------------------------------------------
# see separate file snippetsGistempPlot.py







# Tutorial 8: Calculate & plot global temp mean at each time
# ------------------------------------------

# VECTORIZED CALCULATION OF THE MEAN
monthlyMeanAnomVec = np.nanmean(anomAll,axis=(1,2))


# ALTERNATIVE (in loop, not vectorized!!!):
# getting the number of months in the dataset (we know its 24)
NoOfMonths = len(time)  
# creating a numpy array of the same length, containing zeros
monthlyMeanAnom = np.zeros(NoOfMonths) 
# iterating over each month in a for-loop: estimating mean 'tos' over the globe
for t in range(NoOfMonths):            
    # using nanmean to make sure nan values are ignored
    monthlyMeanAnom[t] = np.nanmean(anomAll[t])


# plotting the time series of mean 'tos' (over the entire globe)
plt.plot(range(NoOfMonths),monthlyMeanAnom)

# adding labels
plt.title("Temperature Anomaly")
plt.xlabel('Months since 01/1880')
plt.ylabel('Temperature (Celsius)')

