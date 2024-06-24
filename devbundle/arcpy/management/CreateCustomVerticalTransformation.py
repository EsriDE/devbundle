# Generated documentation for module arcpy.management


class CreateCustomVerticalTransformation(object):
    """
    Creates a transformation definition for converting data between two vertical coordinate systems or datums. The output of this tool can be used as a transformation object for any tool with a parameter that requires a vertical transformation.
    """

    @property
    def description(self) -> str:
        return """

        CreateCustomVerticalTransformation_management(vt_name, source_vt_coor_system, target_vt_coor_system, {interpolation_gcs}, {custom_vt}, {extent}, {accuracy})

        Creates a transformation definition for converting data between two
        vertical coordinate systems or datums. The output of this tool can be
        used as a transformation object for any tool with a parameter that
        requires a vertical transformation.

     INPUTS:
      vt_name (String):
          The name of the custom transformation definition.
      source_vt_coor_system (String):
          The starting vertical coordinate system.
      target_vt_coor_system (String):
          The final vertical coordinate system.
      interpolation_gcs {Coordinate System}:
          The interpolation geographic coordinate system.This parameter is only
          active if a vertical transformation method
          requires it.The geographic coordinate system is used when
          interpolating the offset
          values from a file, or latitude and longitude coordinates are required
          by the method. The methods that do not require an interpolation
          geographic coordinate system are Null, Unit Change, Height Depth
          Reversal, and Vertical Offset.
      custom_vt {String}:
          The vertical transformation method.From the drop-down list, choose the
          transformation method that will be
          used to transform the data from the input vertical coordinate system
          to the output vertical coordinate system. Once chosen, its parameters
          will appear in the table for editing.A list of the methods and
          parameters is available in the.If using a method that requires a file,
          see the Usage Notes for where
          to put the file or files.
      extent {Extent}:
          The extent where the transformation is applicable.Use WGS84 (WKID:
          4326) or another GNSS-based geographic coordinate
          system such as NAD 1983 or GDA2020 for the extent coordinate system.
          If a projected coordinate system or a layer that has a projected
          coordinate system is provided, the values will be converted to
          latitude and longitude.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      accuracy {Double}:
          A general statement of accuracy in meters.

        """