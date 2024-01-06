import netCDF4 as nc
from pyvtk import VtkData, StructuredGrid, PointData, Scalars
import numpy as np

netcdf_file_path = 'oceandata_temperature.nc'
dataset = nc.Dataset(netcdf_file_path, 'r')

# Extract longitude, latitude, and time dimensions
lon = dataset.variables['lon'][:]
lat = dataset.variables['lat'][:]
time = dataset.variables['time'][:]

# Extract the 'analysed_sst' variable (sea surface temperature)
analysed_sst = dataset.variables['analysed_sst'][:] * dataset.variables['analysed_sst'].scale_factor + dataset.variables['analysed_sst'].add_offset

points = [(loni, lati, 0) for lati in lat for loni in lon]
grid = StructuredGrid([len(lon), len(lat), 1], points)
sst_flat = analysed_sst.ravel()
data = PointData(Scalars(sst_flat, name='analysed_sst'))
vtk_data = VtkData(grid, data)
vtk_file_path = 'oceandata_temperature.vtk'

vtk_data.tofile(vtk_file_path)

dataset.close()