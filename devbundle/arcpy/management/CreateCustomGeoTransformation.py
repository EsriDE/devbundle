# Generated documentation for module arcpy.management


class CreateCustomGeoTransformation(object):
    """
    Creates a transformation definition for converting data between two geographic coordinate systems or datums. The output of this tool can be used as a transformation for any tool with a parameter that requires a geographic transformation.
    """

    @property
    def description(self) -> str:
        return """

        CreateCustomGeoTransformation_management(geot_name, in_coor_system, out_coor_system, custom_geot)

        Creates a transformation definition for converting data between two
        geographic coordinate systems or datums. The output of this tool can
        be used as a transformation for any tool with a parameter that
        requires a geographic transformation.

     INPUTS:
      geot_name (String):
          The name of the custom transformation definition.
      in_coor_system (Coordinate System):
          The starting geographic coordinate system.
      out_coor_system (Coordinate System):
          The final geographic coordinate system.
      custom_geot (String):
          The custom transformation method.A list of the methods and parameters
          is available in the.Set the METHOD and PARAMETER values wrapped in a
          string for custom
          transformation GEOGTRAN. Set the name of the method from the available
          methods of Geocentric_Translation, Molodensky, Molodensky_Abridged,
          Position_Vector, Coordinate_Frame, Molodensky_Badekas, NADCON, HARN,
          NTV2, Longitude_Rotation, Unit_Change, and Geographic_2D_Offset. Each
          method has a set of parameters. You can edit the option values by
          entering text next to the name of the parameter within the whole
          string representation of the custom geographic transformation. See
          examples in the Python sample below.

        """