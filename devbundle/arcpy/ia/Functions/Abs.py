# Generated documentation for module arcpy.ia.Functions


class Abs(object):
    """
    Calculates the absolute value of the cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Abs_ia(in_raster_or_constant)

        Calculates the absolute value of the cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster for which to calculate the absolute values.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the absolute value of the cells
          of the input
          raster.

        """