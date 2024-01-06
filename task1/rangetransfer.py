import xarray as xr
rawnc_path='data.nc'
ds=xr.open_dataset(rawnc_path)
lon_name = 'X'  #你的nc文件中经度的命名
ds['X_adjust'] = xr.where(
    ds[lon_name] > 180,
    ds[lon_name] - 360,
    ds[lon_name])
ds = (ds.swap_dims({lon_name: 'X_adjust'})
    .sel(**{'X_adjust': sorted(ds.longitude_adjusted)})
    .drop(lon_name))
ds = ds.rename({'X_adjust': lon_name})
ds.to_netcdf(Outpath)