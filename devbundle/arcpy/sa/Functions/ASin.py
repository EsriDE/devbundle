# Generated documentation for module arcpy.sa.Functions


class ASin(object):
    """
    Calculates the inverse sine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        ASin_sa(in_raster_or_constant)

        Calculates the inverse sine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the inverse sine values.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the inverse sine of the input values.

        """