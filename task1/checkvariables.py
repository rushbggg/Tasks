import netCDF4 as nc


file_path = "oceandata_temperature.nc"
file_obj = nc.Dataset(file_path)
print (file_obj.variables.keys())
# #
lon = file_obj.variables['lon'] #Longitude 精度
lat = file_obj.variables['lat'] #latitude 维度
sea_ice_fraction = file_obj.variables['sea_ice_fraction'] #sea ice area fraction 海冰面积比值
T = file_obj.variables['time'] #reference time of SST field SST场参考时间
analysed_sst = file_obj.variables['analysed_sst'] #analysed sea surface temperature 分析的海面温度
analysis_error = file_obj.variables['analysis_error'] #estimated error standard deviation of analysed_sst, analysis_sst 的估计误差标准差
mask = file_obj.variables['mask'] #sea/land/lake/ice field composite mask 海/陆/湖/冰原复合罩
crs = file_obj.variables['crs'] #coordinate reference system 坐标参考系

print (lon, lat, sea_ice_fraction, T, analysed_sst, analysis_error,mask,crs)


