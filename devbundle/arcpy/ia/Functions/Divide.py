# Generated documentation for module arcpy.ia.Functions


class Divide(object):
    """
    Divides the values of two rasters on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Divide_ia(in_raster_or_constant1, in_raster_or_constant2)

        Divides the values of two rasters on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input whose values will be divided by the second input.A number
          can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input whose values the first input are to be divided by.A number
          can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the quotient of the first input
          raster (dividend)
          divided by the second input (divisor).

        """