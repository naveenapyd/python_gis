# Format Conversion

## Overview

A python program that can convert shapefiles `.shp` into a `.geojson` format, using `geopandas`.

## Getting Started

### Prerequisites

`Python 3.14`

- `geopandas` - Geospatial tabular data manipulation

### Setup

Install following library:

```
pip install geopandas
```

OR

```
conda install geopandas
```

### Run the program

Run the following in a terminal open in the folder `format_conversion`:

```
python3 format_conversion.py
```

OR

Open `format_conversion` folder in VSCode and navigate to `format_conversion.py` and then press `F5`.

## Project Specifics

1. The script expects the input file name to be `test_points.shp` in the `Inputs` sub-directory.
2. If your input file is not in `WGS84`, then it will automatically be reprojected to this `CRS`.
3. The output file will get stored in the `Outputs` sub-directory as `test_points.geojson`.
