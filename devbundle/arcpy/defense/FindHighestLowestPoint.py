# Generated documentation for module arcpy.defense


class FindHighestLowestPoint(object):
    """
    Finds the highest or lowest point of the input surface within a defined area.
    """

    @property
    def description(self) -> str:
        return """

        FindHighestLowestPoint_defense(in_surface, out_feature_class, high_low_operation_type, {in_feature})

        Finds the highest or lowest point of the input surface within a
        defined area.

     INPUTS:
      in_surface (Raster Layer / Mosaic Dataset / Mosaic Layer):
          The input elevation raster surface.
      high_low_operation_type (String):
          Specifies the type of operation the tool will perform.HIGHEST-The
          highest points will be found. This is the
          default.LOWEST-The lowest points will be found.
      in_feature {Feature Set}:
          The input polygon feature class within which the highest or lowest
          point will be found.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output highest or lowest point.

        """