# Generated documentation for module arcpy.ia.Functions


class ACosH(object):
    """
    Calculates the inverse hyperbolic cosine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        ACosH_ia(in_raster_or_constant)

        Calculates the inverse hyperbolic cosine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the inverse hyperbolic cosine
          values.To use a number as an input for this parameter, the cell size
          and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the inverse hyperbolic cosine of the
          input values.

        """