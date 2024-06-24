# Generated documentation for module arcpy.sa.Functions


class Cos(object):
    """
    Calculates the cosine of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Cos_sa(in_raster_or_constant)

        Calculates the cosine of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input for which to calculate the cosine values.To use a number as
          an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the cosine of the input values.

        """