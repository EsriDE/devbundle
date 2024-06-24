# Generated documentation for module arcpy.ia.Functions


class Sin(object):
    """
    Calculates the sine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Sin_ia(in_raster_or_constant)

        Calculates the sine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the sine values.To use a number as an
          input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the sine of the input values.

        """