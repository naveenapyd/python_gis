import pdal

json_file = "transform_laz.json"
with open(json_file, "r") as file:
    pipeline_data = file.read()

pipeline = pdal.Pipeline(pipeline_data)
pipeline.execute()
