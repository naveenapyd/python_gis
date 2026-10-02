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

## Project Specifics

1. The input file format is hard coded to `input_ellipsoidal.xlsx`, and in the root directory.
2. The co-ordinate values in the excel should be in one column under the columns name `Location`.
3. The format for the co-ordinate values should be UTM co-ordinates $(Easting, Northing, Elevation)$  
	`X: 377113.075, Y: 2192736.485, Z: -30.083`
4. The output file `output_orthometric.csv` can be found in the same directory as the input file. 
