# Orthometric Height Conversion

## Overview

A python program that reads spatial coordinates from an excel file, parses UTM $(x, y, z)$ point data, and converts the ellipsoidal heights into orthometric heights, using `pandas` and `pyproj`.

## Getting Started

### Prerequisites

`Python 3.14`  
- `pandas` - Tabular data manipulation
- `openpyxl` - Excel file I/O engine for `pandas`
- `pyproj` - Python interface to PROJ (handling `CRS`, `Transformer`, `TransformerGroup`, and `network`)

### Setup

Install following libraries:

```
pip install pandas openpyxl pyproj
```

OR

```
conda install pandas openpyxl pyproj
```

### Run the program

Run the following in a terminal open in the folder `coord_transform`:

```
python3 coord_transform.py
```

OR

Open `coord_transform` folder in VSCode and navigate to `coord_transform.py` and then press `F5`.

## Project Specifics

1. The input file format is hard coded to `input_ellipsoidal.xlsx` in the root directory, and the output file `output_orthometric_csv` can be found in the same directory.
2. The co-ordinate values in the excel should be in one column under the columns name `Location`.
3. The format for the co-ordinate values should be UTM co-ordinates $(Easting, Northing, Elevation)$ as shown,   
			`X: 377113.075, Y: 2192736.485, Z: -30.083`
4. The UTM zone of the points in the input file should be known. The CRS used here is `EPSG:32645`. This can be changed according to your input file's CRS in **line 42** of the code.