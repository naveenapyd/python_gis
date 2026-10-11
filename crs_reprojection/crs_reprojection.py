import pandas as pd
from pyproj import CRS, Transformer

# define input paths
csv_path = r'.\Inputs\input_points_wgs84.csv'
utm_zones_csv = r'.\Inputs\world_utm_zones.csv'

# define output paths
csv_output = r'.\Outputs\output_points_utm.csv'

# load the csv file into a dataframe
df1 = pd.read_csv(csv_path)
utm_df = pd.read_csv(utm_zones_csv)

print('The input dataframe is:\n')
print(df1.head())

# using the utm_df check the points in the df1 as to they belong to which utm zone
for index, value in enumerate(df1['Longitude']):
    matching_row = utm_df[(utm_df['Longitude A'] <= value) & (utm_df['Longitude B'] > value)]

    if matching_row.empty:
        print(f'The longitude {value} donot fit in any zone in the database')
    else:
        print(f'Matching row for {value} is {matching_row}')
        utm_zone = matching_row.iloc[0,0]
        if df1.loc[index, 'Latitude'] >= 0:
            # zero is included for positive values as 0 deg latitude is typically included in northern hemisphere
            epsg_code = '326' + str(utm_zone)
            print(epsg_code)         
        else:
            epsg_code = '327' + str(utm_zone)
            print(epsg_code)
        
        # add EPSG to a new column
        df1.loc[index, 'EPSG'] = epsg_code

        # define the input and output CRS
        input_CRS = CRS.from_epsg(4326)
        output_CRS = CRS.from_epsg(epsg_code)
        
        # intialize transformer
        # 'always_xy = True' argument ensures order as Easting, Northing / Longitude, Latitude
        wgs_to_utm = Transformer.from_crs(input_CRS, output_CRS, always_xy = True)

        # use transformer to convert from one CRS to the other
        df1['Easting'], df1['Northing'] = wgs_to_utm.transform(df1['Longitude'].values , df1['Latitude'].values)

        # round off the floating point numbers to 3 decimals
        df1['Easting'] = df1['Easting'].round(3)
        df1['Northing'] = df1['Northing'].round(3)

        # store the output in the output file
        df1.to_csv(csv_output, index = False)
