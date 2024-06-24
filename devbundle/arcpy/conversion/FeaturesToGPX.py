# Generated documentation for module arcpy.conversion


class FeaturesToGPX(object):
    """
    Converts point, multipoint, or polyline features to a GPX format file (.gpx).
    """

    @property
    def description(self) -> str:
        return """

        FeaturesToGPX_conversion(in_features, out_gpx_file, {name_field}, {description_field}, {z_field}, {date_field})

        Converts point, multipoint, or polyline features to a GPX format file
        (.gpx).

     INPUTS:
      in_features (Feature Layer):
          The input point, multipoint, or line features.
      name_field {Field}:
          A field from the input features with values used to populate the GPX
          name tag.
      description_field {Field}:
          A field from the input features with values used to populate the GPX
          desc tag.
      z_field {Field}:
          A numeric field from the input features with values used to populate
          the GPX elevation tag. If an elevation field is not specified, the
          z-values from the input features' geometries will be used to populate
          the GPX elevation tag.
      date_field {Field}:
          A date/time field from the input features with values used to populate
          the GPX time tag.

     OUTPUTS:
      out_gpx_file (File):
          The .gpx file that will be created with the geometry and attributes of
          the input features.

        """