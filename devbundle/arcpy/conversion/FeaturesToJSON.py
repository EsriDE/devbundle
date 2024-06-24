# Generated documentation for module arcpy.conversion


class FeaturesToJSON(object):
    """
    Converts features to Esri JSON or GeoJSON format. The fields, geometry, and spatial reference of features will be converted to their corresponding JSON representation and written to a file with a .json or .geojson extension.
    """

    @property
    def description(self) -> str:
        return """

        FeaturesToJSON_conversion(in_features, out_json_file, {format_json}, {include_z_values}, {include_m_values}, {geoJSON}, {outputToWGS84}, {use_field_alias})

        Converts features to Esri JSON or GeoJSON format. The fields,
        geometry, and spatial reference of features will be converted to their
        corresponding JSON representation and written to a file with a .json
        or .geojson extension.

     INPUTS:
      in_features (Feature Layer):
          The features to convert to JSON format.
      format_json {Boolean}:
          Specifies whether the JSON will be formatted to improve readability
          similar to the ArcGIS REST API specification's PJSON (Pretty JSON)
          format.NOT_FORMATTED-The features will not be formatted. This is the
          default.FORMATTED-The features will be formatted to improve
          readability.
      include_z_values {Boolean}:
          Specifies whether the z-values of the features will be included in the
          JSON.NO_Z_VALUES-The z-values will not be included in geometries, and
          the
          hasZ property of the JSON will not be included. This is the
          default.Z_VALUES-The z-values will be included in geometries, and the
          hasZ
          property of the JSON will be set to true.
      include_m_values {Boolean}:
          Specifies whether the m-values of the features will be included in the
          JSON.NO_M_VALUES-The m-values will not be included in geometries, and
          the
          hasM property of the JSON will not be included. This is the
          default.M_VALUES-The m-values will be included in geometries, and the
          hasM
          property of the JSON will be set to true.
      geoJSON {Boolean}:
          Specifies whether the output will be created in GeoJSON format,
          conforming to the GeoJSON specification.GEOJSON-The output will be
          created in GeoJSON format (.geojson
          file).NO_GEOJSON-The output will be created in Esri JSON format (.json
          file). This is the default.
      outputToWGS84 {Boolean}:
          Specifies whether the input features will be projected to the
          geographic coordinate system WGS_1984 with a default geographic
          transformation. This parameter only applies when the output is
          GeoJSON.WGS84-Features will be projected to
          WGS_1984.KEEP_INPUT_SR-Features
          will not be projected to WGS_1984. The GeoJSON
          will contain a CRS tag that defines the coordinate system. This is the
          default.
      use_field_alias {Boolean}:
          Specifies whether the output file will use field aliases for feature
          attributes.USE_FIELD_NAME-Output feature attributes will not use field
          aliases;
          they will use field names. This is the default.USE_FIELD_ALIAS-Output
          feature attributes will use field aliases.

     OUTPUTS:
      out_json_file (File):
          The output .json or .geojson file.

        """