# Generated documentation for module arcpy.sa.Functions


class Square(object):
    """
    Calculates the square of the cell values in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Square_sa(in_raster_or_constant)

        Calculates the square of the cell values in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input values to find the square of.To use a number as an input for
          this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the square of the input cell
          values.

        """