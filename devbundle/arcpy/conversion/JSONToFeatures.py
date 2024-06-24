# Generated documentation for module arcpy.conversion


class JSONToFeatures(object):
    """
    Converts feature collections in an Esri JSON formatted file (.json) or a GeoJSON formatted file (.geojson) to a feature class.
    """

    @property
    def description(self) -> str:
        return """

        JSONToFeatures_conversion(in_json_file, out_features, {geometry_type})

        Converts feature collections in an Esri JSON formatted file (.json) or
        a GeoJSON formatted file (.geojson) to a feature class.

     INPUTS:
      in_json_file (File):
          The input .json or .geojson file that will be converted to a feature
          class.The input file extension determines the format used by the tool
          for
          proper conversion. For Esri JSON formatted file, use the .json
          extension; for GeoJSON formatted files, use the .geojson extension.
      geometry_type {String}:
          Specifies the geometry type that will be used to convert from GeoJSON
          to features. This parameter is only used when the input is a .geojson
          file. If the .geojson file does not contain any of the specified
          geometry types, the output feature class will be empty.POINT-Points
          will be converted to features.MULTIPOINT-Multipoints will
          be converted to features.POLYLINE-Polylines will be converted to
          features.POLYGON-Polygons will be converted to features.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class that will contain the features from the input
          .json or .geojson file.

        """