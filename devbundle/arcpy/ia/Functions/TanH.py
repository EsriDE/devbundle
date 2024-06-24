# Generated documentation for module arcpy.ia.Functions


class TanH(object):
    """
    Calculates the hyperbolic tangent of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        TanH_ia(in_raster_or_constant)

        Calculates the hyperbolic tangent of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input to calculate the hyperbolic tangent values for.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the hyperbolic tangent of the input
          values.

        """