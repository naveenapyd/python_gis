import pandas as pd
from pyproj import CRS, Transformer
from pyproj.transformer import TransformerGroup
from pyproj import network

network.set_network_enabled(True)

tg = TransformerGroup('epsg:4979', 'epsg:9518')
tg.download_grids(verbose = True)

def main():
    # define input and output files
    input_file = 'coord_transform/Panel_Antenna_new_Components_2026-02-11.xlsx'
    output_csv = 'coord_transform/Test.csv'

    # store excel as data frame, which is like an array in pandas
    df_input = pd.read_excel(input_file, skiprows = 4)

    # split the 'AGL Height' column
    # 'expand = True' argument turns a list of split strings into separate columns
    split_xyz_col = df_input['Agl height'].str.split(',', expand = True)

    # add and name the new columns
    df_input[['X', 'Y', 'Z']] = split_xyz_col

    # split the 'X' column; add new columns
    split_x_col = df_input['X'].str.split(':', expand = True)
    df_input[['just_x', 'easting']] = split_x_col

    # split the 'Y' column; add new columns
    split_y_col = df_input['Y'].str.split(':', expand = True)
    df_input[['just_y', 'northing']] = split_y_col

    # split the 'Z' column; add new columns
    split_z_col = df_input['Z'].str.split(':', expand = True)
    df_input[['just_z', 'ellipsoidal_height']] = split_z_col

    # delete the unnecessary columns
    unnecessary_cols = ['Agl height', 'X', 'Y', 'Z', 'just_x', 'just_y', 'just_z']
    df_input = df_input.drop(columns = unnecessary_cols)

    # define input and output CRS 
    xy_input_CRS = CRS.from_epsg(32645)
    xy_output_CRS = CRS.from_epsg(4326)

    # transformer to convert easting, northing to long, lat
    # 'always_xy = True' argument ensures order as Easting, Northing / Longitude, Latitude
    # using the transformer to convert
    utm_to_wgs = Transformer.from_crs(xy_input_CRS, xy_output_CRS, always_xy = True)
    df_input['long'], df_input['lat'] = utm_to_wgs.transform(df_input['easting'].values , df_input['northing'].values)

    # define input and output CRS 
    # 'epsg:4979' is the code for WGS84 with ellipsoidal height
    # 'epsg:9518' is the code for WGS84 EGM2008
    z_input_CRS = CRS.from_epsg(4979) 
    z_output_CRS = CRS.from_epsg(9518)

    # transformer to convert ellipsoidal to orthometric 
    # 'always_xy = True' argument is used because GCS order is Latitude, Lomgitude
    # using the transformer to convert
    # direction = 'VERT_ELLIPSOID_TO_ORTHO' argument specifies conversion directions
    ellip_to_ortho = Transformer.from_crs(z_input_CRS, z_output_CRS, always_xy = True)
    df_input['orthometric_height'] = ellip_to_ortho.transform(
        df_input['long'].values, 
        df_input['lat'].values, 
        df_input['ellipsoidal_height'].values
    )[2]
    
    # write this output data frame to the output csv
    # 'index = False' argument prevents pandas from writing the data frame as a column
    df_input.to_csv(output_csv, index = False)
    return True

main()