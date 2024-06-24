# Generated documentation for module arcpy.ia.Functions


class CosH(object):
    """
    Calculates the hyperbolic cosine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        CosH_ia(in_raster_or_constant)

        Calculates the hyperbolic cosine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the hyperbolic cosine values.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the hyperbolic cosine of the input
          values.

        """