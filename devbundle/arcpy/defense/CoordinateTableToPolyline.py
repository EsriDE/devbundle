# Generated documentation for module arcpy.defense


class CoordinateTableToPolyline(object):
    """
    Creates a polyline feature class from coordinates stored in a table.
    """

    @property
    def description(self) -> str:
        return """

        CoordinateTableToPolyline_defense(in_table, out_feature_class, x_or_lon_field, in_coordinate_format, {y_or_lat_field}, {line_group_field}, {sort_field}, {coordinate_system})

        Creates a polyline feature class from coordinates stored in a table.

     INPUTS:
      in_table (Table View):
          The table containing the source coordinates.
      x_or_lon_field (Field):
          The field in the input table containing the x or longitude
          coordinates.
      in_coordinate_format (String):
          Specifies the format of the input table coordinates.DD_1-Coordinates
          will be formatted in a decimal degrees coordinate
          pair stored in a single field with coordinates separated by a space,
          comma, or slash.DD_2-Coordinates will be formatted in a decimal
          degrees coordinate
          pair stored in two table fields. This is the default.DDM_1-Coordinates
          will be formatted in a degrees and decimal minutes
          coordinate pair stored in a single table field with coordinates
          separated by a space, comma, or slash.DDM_2-Coordinates will be
          formatted in a degrees and decimal minutes
          coordinate pair stored in two table fields.DMS_1-Coordinates will be
          formatted in a degrees, minutes, and seconds
          coordinate pair stored in a single table field with coordinates
          separated by a space, comma, or slash.DMS_2-Coordinates will be
          formatted in a degrees, minutes, and seconds
          coordinate pair stored in two table fields.GARS-Coordinates will be
          formatted in Global Area Reference System.GEOREF-Coordinates will be
          formatted in World Geographic Reference
          System.UTM_BANDS-Coordinates will be formatted in Universal Transverse
          Mercator coordinate bands.UTM_ZONES-Coordinates will be formatted in
          Universal Transverse
          Mercator coordinate zones.USNG-Coordinates will be formatted in United
          States National Grid.MGRS-Coordinates will be formatted in Military
          Grid Reference System.
      y_or_lat_field {Field}:
          The field in the input table containing the y or latitude
          coordinates.The y_or_lat_field parameter is used when the
          in_coordinate_format
          parameter is set to DD_2, DDM_2, or DMS_2.
      line_group_field {Field}:
          The field in the input table field used to create unique polylines. A
          polyline will be created for each unique value.
      sort_field {Field}:
          The field in the input table used to order the polyline vertices. The
          field must be numeric.
      coordinate_system {Spatial Reference}:
          The spatial reference of the output feature class. The default is
          GCS_WGS_1984.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output polyline features.

        """