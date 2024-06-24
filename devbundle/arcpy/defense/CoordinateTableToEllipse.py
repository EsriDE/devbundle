# Generated documentation for module arcpy.defense


class CoordinateTableToEllipse(object):
    """
    Creates ellipse features from coordinates stored in a table and input data values.
    """

    @property
    def description(self) -> str:
        return """

        CoordinateTableToEllipse_defense(in_table, out_feature_class, x_or_lon_field, major_field, minor_field, in_coordinate_format, {distance_units}, {y_or_lat_field}, {azimuth_field}, {azimuth_units}, {coordinate_system})

        Creates ellipse features from coordinates stored in a table and input
        data values.

     INPUTS:
      in_table (Table View):
          The table containing the source coordinates.
      x_or_lon_field (Field):
          The field in the input table containing the x or longitude
          coordinates.
      major_field (Field):
          The field in the input table containing the major axis values.
      minor_field (Field):
          The field in the input table containing the minor axis values.
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
      distance_units {String}:
          Specifies the unit of measurement for the major and minor
          axes.METERS-The unit will be meters. This is the
          default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      y_or_lat_field {Field}:
          The field in the input table containing the latitude coordinates.The
          y_or_lat_field parameter is used when the in_coordinate_format
          parameter is set to DD_2, DDM_2, or DMS_2.
      azimuth_field {Field}:
          The field in the input table containing the ellipse azimuth values.
      azimuth_units {String}:
          Specifies the unit of measurement for the azimuth field.DEGREES-The
          angle will be degrees. This is the default.MILS-The angle
          will be mils.RADS-The angle will be radians.GRADS-The angle will be
          gradians.
      coordinate_system {Spatial Reference}:
          The spatial reference of the output feature class. The default is
          GCS_WGS_1984.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output ellipse polygon features.

        """