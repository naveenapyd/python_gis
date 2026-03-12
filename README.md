
# Reprojection of elevation values from ellipsoidal to orthometric

## Setup

### For a set of points stored in an excel

Install following libraries:
```
pip install pandas
# OR
conda install pandas
```

```
pip install pyproj
# OR
conda install pyproj
```

Run `F5` on [coord_transform_excel.py](./coord_transform_excel.py)

### For a point cloud (.las)

Install GDAL
```
conda install gdal
```

Install [PDAL python bindings](https://pdal.io/en/2.8.4/python.html) in conda, which also installs the base PDAL library automatically

Install in existing environment other than base:
```
conda install -n <environment name> -c conda-forge python-pdal
```

To create a new environment and install pdal in it, use:
```
conda create -n <environment name> -c conda-forge python-pdal
conda activate <environment name>
```

In VSCode, Open Command Palette `Ctrl + Shift + P` and choose `Python: Select Interpreter` to choose the environment created in conda.

Run `F5` on [coord_transform_las.py](./coord_transform_las.py) which uses [ellip_to_orthometric.json](./ellip_to_orthometric.json) as input.

## Project specifics

In order for the conversion to take place, the appropriate geoid file should be stored in gdal database.

Geoid .gtx files can be downloaded from [here](https://download.osgeo.org/proj/vdatum/)  
Geoid .tif files can be downloaded from [here](https://www.agisoft.com/downloads/geoids/)

The input point cloud used here is in UTM Zone 45N `EPSG : 32645`. 
Since, the geoid files are in WGS84 `EPSG : 4326`, the point cloud is first reprojected from UTM 45N to WGS84. 

The ellipsoidal height values in WGS84 `EPSG : 4979` can now be converted to orthometric height values in WGS84 `EPSG : 9518`. 
Here, for the input CRS, `EPSG : 4979` is used instead of `EPSG : 4326`, because the latter stores only 2D values (only lat, long), while the former stores 3D values (lat, long, elev). 
Further, for the output CRS, `EPSG : 9518`, which is equivalent to `EPSG : 4326 + 3855` is used as `EGM2008` geoid is stored in the database.

You can now simply reproject your point cloud back from WGS84 to UTM 45N. 


