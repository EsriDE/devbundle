# Generated documentation for module arcpy.ia.Functions


class Exp2(object):
    """
    Calculates the base 2 exponential of the cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Exp2_ia(in_raster_or_constant)

        Calculates the base 2 exponential of the cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input values for which to find the base 2 exponential.To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the base 2 exponential of the
          input values.

        """