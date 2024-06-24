# Generated documentation for module arcpy.ia.Functions


class RoundUp(object):
    """
    Returns the next higher integer value, just represented as a floating point, for each cell in a raster.
    """

    @property
    def description(self) -> str:
        return """

        RoundUp_ia(in_raster_or_constant)

        Returns the next higher integer value, just represented as a floating
        point, for each cell in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input values to be rounded up.To use a number as an input for this
          parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of rounding up the
          input values.

        """