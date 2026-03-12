import pdal

def main():
    json_file = "utm_to_wgs_ellip_to_ortho_wgs_to_utm.json"
    with open(json_file, "r") as file:
        pipeline_data = file.read()

    pipeline = pdal.Pipeline(pipeline_data)
    count = pipeline.execute()
    print(f"Number of points processed: {count}")
    return True

main()