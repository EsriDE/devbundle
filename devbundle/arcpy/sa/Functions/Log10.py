# Generated documentation for module arcpy.sa.Functions


class Log10(object):
    """
    Calculates the base 10 logarithm of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Log10_sa(in_raster_or_constant)

        Calculates the base 10 logarithm of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          Input values for which to find the base 10 logarithm.To use a number
          as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the base 10 logarithm of the
          input values.

        """