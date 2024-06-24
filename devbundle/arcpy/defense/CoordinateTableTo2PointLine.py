# Generated documentation for module arcpy.defense


class CoordinateTableTo2PointLine(object):
    """
    Creates 2-point line features from coordinates stored in a table.
    """

    @property
    def description(self) -> str:
        return """

        CoordinateTableTo2PointLine_defense(in_table, out_feature_class, start_x_or_lon_field, end_x_or_lon_field, in_coordinate_format, {start_y_or_lat_field}, {end_y_or_lat_field}, {line_type}, {coordinate_system})

        Creates 2-point line features from coordinates stored in a table.

     INPUTS:
      in_table (Table View):
          The table containing the source coordinates.
      start_x_or_lon_field (Field):
          The field in the input table containing the starting x or longitude
          coordinates.
      end_x_or_lon_field (Field):
          The field in the input table containing the ending x or longitude
          coordinates.
      in_coordinate_format (String):
          Specifies the format of the point coordinates.DD_1-Coordinates will be
          formatted in a decimal degrees coordinate
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
      start_y_or_lat_field {Field}:
          The field in the input table containing the starting y or latitude
          coordinates.The start_y_or_lat_field parameter is used when the
          in_coordinate_format parameter is set to DD_2, DDM_2, or DMS_2.
      end_y_or_lat_field {Field}:
          The field in the input table containing the ending y or latitude
          coordinates.The end_y_or_lat_field parameter is used when the
          in_coordinate_format
          parameter is set to DD_2, DDM_2, or DMS_2.
      line_type {String}:
          Specifies the output line type.GEODESIC-The shortest distance between
          any two points on the earth's
          spheroidal surface (ellipsoid) will be used. This is the
          default.GREAT_CIRCLE-The line on a spheroid (ellipsoid) defined by the
          intersection of a plane passing through the center of the spheroid
          will be used.RHUMB_LINE-A line of constant bearing or azimuth will be
          used.NORMAL_SECTION-A normal plane to the earth's ellipsoidal surface
          containing the start and end points will be used.
      coordinate_system {Spatial Reference}:
          The spatial reference of the output feature class. The default is
          GCS_WGS_1984.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output line features.

        """