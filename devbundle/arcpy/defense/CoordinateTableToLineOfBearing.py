# Generated documentation for module arcpy.defense


class CoordinateTableToLineOfBearing(object):
    """
    Creates lines of bearing from coordinates stored in a table.
    """

    @property
    def description(self) -> str:
        return """

        CoordinateTableToLineOfBearing_defense(in_table, out_feature_class, x_or_lon_field, bearing_field, distance_field, in_coordinate_format, {bearing_units}, {distance_units}, {y_or_lat_field}, {line_type}, {coordinate_system})

        Creates lines of bearing from coordinates stored in a table.

     INPUTS:
      in_table (Table View):
          The table containing the source coordinates.
      x_or_lon_field (Field):
          The field in the input table containing the x or longitude
          coordinates.
      bearing_field (Field):
          The field in the input table containing the bearing values.
      distance_field (Field):
          The field in the input table containing the distance values.
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
      bearing_units {String}:
          Specifies the unit of measurement for the bearing angles.DEGREES-The
          angle will be degrees. This is the default.MILS-The angle
          will be mils.RADS-The angle will be radians.GRADS-The angle will be
          gradians.
      distance_units {String}:
          Specifies the units of measurement for the distance.METERS-The unit
          will be meters. This is the default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      y_or_lat_field {Field}:
          The field in the input table containing the y or latitude
          coordinates.The y_or_lat_field parameter is used when the
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
          The feature class containing the output lines of bearing.

        """