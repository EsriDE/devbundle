# Generated documentation for module arcpy.sa.Functions


class Minus(object):
    """
    Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Minus_sa(in_raster_or_constant1, in_raster_or_constant2)

        Subtracts the value of the second input raster from the value of the
        first input raster on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input from which to subtract the values in the second input.A
          number can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input values to subtract from the values in the first input.A
          number can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of subtracting the
          second input from
          the first.

        """