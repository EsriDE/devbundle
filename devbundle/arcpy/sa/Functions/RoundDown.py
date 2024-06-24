# Generated documentation for module arcpy.sa.Functions


class RoundDown(object):
    """
    Returns the next lower integer value, just represented as a floating point, for each cell in a raster.
    """

    @property
    def description(self) -> str:
        return """

        RoundDown_sa(in_raster_or_constant)

        Returns the next lower integer value, just represented as a floating
        point, for each cell in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input values to be rounded down.To use a number as an input for
          this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of rounding down the
          input values.

        """