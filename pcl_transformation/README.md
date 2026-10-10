# Point Cloud Transformation using PDAL

## Overview

A python program that reads spatial coordinates for point cloud `.laz` files, parses UTM $(x, y, z)$ point data, converts the point cloud from **Geodetic System 1984 ensemble** to **UTM System**, and merges all the point cloud tiles to one `.laz` file, using `PDAL` pipeline.
```
NOTE:
Input files are not provided in this project
```

## Getting Started

### Prerequisites

`Python 3.14`  
- `pdal` - python bindings of the PDAL library

### Setup

It is recommended to install PDAL in an environment other than the base environment. And it is also recommended to install the PDAL python support using the Conda package manager. When package is installed using Conda package manager, all its dependent packages will get installed as well.

Install using Conda:

To create a new environment, activate the environment, and install:
```
conda create --name <environment name>
conda activate <environment name>
conda install -c conda-forge pdal
```

Further details and the installation of PDAL using pip can be found [here](https://pdal.io/en/2.9.0/python.html)

### Run the program

Run the following in a terminal open in the folder `pcl_transformation`:

```
python3 transform_laz.py
```

OR

Open `pcl_transformation` folder in VSCode and navigate to `transform_laz.py` and then press `F5`.

## Project Specifics

1. The structure of the code is as follows:
```
transform_laz.json    # PDAL pipeline definition (reader, reprojection, writer(with merger))
transform_laz.py      # python script to load and execute the pipeline
```
2. The CRS of the input point cloud files should be known. The CRS of the input files used here is `EPSG:4978`. This can be changed according to your specifications in the `transform_laz.json` file.
3. Similarly, the output CRS to which you need the `.laz` files to be converted should also be specified. The CRS for conversion used here is `UTM Zone 43N` whose code is `EPSG:32643`. This can be changed according to your specifications in the `transform_laz.json` file.
4. It is ideal to transform the output file on the same specifications as the input file. Hence, the values for other parameters, namely, the `minor_version`, `dataformat_id`, and ` scale` should be specified as present in the input files. These parameters for your input files can be checked in the metadata. 
Using Conda terminal:
Activate where your pdal environment is installed. Navigate to your inputs folder and run the following command to get the metadata of your input file.
```
pdal info input.laz --metadata
```
