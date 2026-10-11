import geopandas as gpd

shapefile_path = r'.\Inputs\test_points.shp'

# Load the shapefile into a geodataframe
shapefile_gdf = gpd.read_file(shapefile_path)

# Check the CRS of the shapefile
print(f'The CRS of the input shapefile is {shapefile_gdf.crs}')

# If the CRS is not WGS84 (EPSG:4326), convert it to WGS84
if shapefile_gdf.crs != 'EPSG:4326':
    shapefile_gdf_wgs = shapefile_gdf.to_crs(epsg=4326)
    print(f'The CRS of the input shapefile is now {shapefile_gdf_wgs.crs}')
    # Save the output file in geojson format
    shapefile_gdf_wgs.to_file(r'.\Outputs\test_points.geojson', driver = 'GeoJSON', index = False)
else:
    shapefile_gdf.to_file(r'.\Outputs\test_points.geojson', driver = 'GeoJSON', index = False)
