# Generated documentation for module arcpy.sa.Functions


class Times(object):
    """
    Multiplies the values of two rasters on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Times_sa(in_raster_or_constant1, in_raster_or_constant2)

        Multiplies the values of two rasters on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input containing the values to be multiplied.A number can be used
          as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input containing the values by which the first input will be
          multiplied.A number can be used as an input for this parameter,
          provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the product of the first input
          multiplied by the
          second.

        """