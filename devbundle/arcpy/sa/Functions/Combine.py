# Generated documentation for module arcpy.sa.Functions


class Combine(object):
    """
    Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.
    """

    @property
    def description(self) -> str:
        return """

        Combine_sa(in_rasters;in_rasters...)

        Combines multiple rasters so that a unique output value is assigned to
        each unique combination of input values.

     INPUTS:
      in_rasters (Composite Geodataset):
          The list of input rasters to be combined.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output combined raster.A unique integer value is assigned to each
          unique combination of input
          values.

        """