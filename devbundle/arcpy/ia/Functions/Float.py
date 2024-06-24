# Generated documentation for module arcpy.ia.Functions


class Float(object):
    """
    Converts each cell value of a raster into a floating-point representation.
    """

    @property
    def description(self) -> str:
        return """

        Float_ia(in_raster_or_constant)

        Converts each cell value of a raster into a floating-point
        representation.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster to be converted to floating point.To use a number as
          an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the floating-point
          representation of the input
          values.

        """