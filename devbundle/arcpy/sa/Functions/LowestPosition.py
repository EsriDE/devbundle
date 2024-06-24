# Generated documentation for module arcpy.sa.Functions


class LowestPosition(object):
    """
    Determines on a cell-by-cell basis the position of the raster with the minimum value in a set of rasters.
    """

    @property
    def description(self) -> str:
        return """

        LowestPosition_sa(in_rasters_or_constants;in_rasters_or_constants...)

        Determines on a cell-by-cell basis the position of the raster with the
        minimum value in a set of rasters.

     INPUTS:
      in_rasters_or_constants (Composite Geodataset):
          The list of input rasters for which the position of the input with the
          lowest value will be determined.A number can be used as an input;
          however, the cell size and extent
          must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.For each cell in the output raster, the value
          represents the position
          of the raster with the lowest value.

        """