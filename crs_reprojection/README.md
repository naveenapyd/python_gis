# CRS Reprojection

## Overview

A python program that reads spatial coordinates of points from a `.csv` file, and converts the `CRS` of the points from `WGS84` to `UTM`.

## Getting Started

### Prerequisites

`Python 3.14`  

- `pandas` - Tabular data manipulation
- `openpyxl` - Excel file I/O engine for `pandas`
- `pyproj` - Python interface to PROJ (handling `CRS`, `Transformer`)

### Setup

Install the following libraries:

```
pip install pandas openpyxl pyproj
```

OR

```
conda install pandas openpyxl pyproj
```

### Run the program

Run the following in a terminal open in the folder `crs_reprojection`:

```
python3 crs_reprojection.py
```

OR

Open `crs_reprojection` folder in VSCode and navigate to `crs_reprojection.py` and then press `F5`.

## Project Specifics

1. The script works only for the conversion of points from `WGS84` system to `UTM` system.
2. The input file format is hard coded to `input_points_wgs84.csv` in the `Inputs` directory.
3. The co-ordinate values in the excel should be in two columns under the names`Latitude` and `Longitude`.
4. There is a `world_utm_zones.csv` file used in the script, which defines the UTM zones. For instance,
`Zone 44 is between 78 and 84 degrees longitudes`
5. The output file `output_points_utm.csv` can be found in the `Outputs` directory.
