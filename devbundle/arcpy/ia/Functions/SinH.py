# Generated documentation for module arcpy.ia.Functions


class SinH(object):
    """
    Calculates the hyperbolic sine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        SinH_ia(in_raster_or_constant)

        Calculates the hyperbolic sine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the hyperbolic sine values.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the hyperbolic sine of the input
          values.

        """