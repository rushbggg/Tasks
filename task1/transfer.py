import netCDF4 as nc
import pyvista as pv
import numpy as np

# 读取.nc文件
nc_file_path = 'oceandata_temperature.nc'
netcdf_data = nc.Dataset(nc_file_path, 'r')

# 获取数据和维度信息
lon = netcdf_data.variables['lon'][:]
print(lon)
# lat = netcdf_data.variables['lat'][:]
# sea_ice_fraction = netcdf_data.variables['sea_ice_fraction'][:]
# T = netcdf_data.variables['time'][:]
# analysed_sst = netcdf_data.variables['analysed_sst'][:]
# analysis_error = netcdf_data.variables['analysis_error'][:]
# mask = netcdf_data.variables['mask'][:]
# crs = netcdf_data.variables['crs'][:]

# print(lon,lat,sea_ice_fraction,T,analysis_error,mask,crs)
# 创建网格
grid = pv.StructuredGrid()

# 添加坐标点
grid.points = np.column_stack((np.repeat(lon, len(lat) * len(T)),
                               np.tile(lat, len(lon) * len(T)),
                               np.tile(T, len(lon) * len(lat))))

# 添加点数据
grid.point_data['sea_ice_fraction'] = sea_ice_fraction.flatten(order='F')
grid.point_data['analysed_sst'] = analysed_sst.flatten(order='F')
grid.point_data['analysis_error'] = analysis_error.flatten(order='F')
grid.point_data['mask'] = mask.flatten(order='F')

# 保存为VTK文件
output_file_path = 'oceandata_temperature.vtk'
grid.save(output_file_path)

# 关闭NetCDF文件
netcdf_data.close()
