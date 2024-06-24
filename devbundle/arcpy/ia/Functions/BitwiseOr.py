# Generated documentation for module arcpy.ia.Functions


class BitwiseOr(object):
    """
    Performs a Bitwise Or operation on the binary values of two input rasters.
    """

    @property
    def description(self) -> str:
        return """

        BitwiseOr_ia(in_raster_or_constant1, in_raster_or_constant2)

        Performs a Bitwise Or operation on the binary values of two input
        rasters.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The first input to use in this bitwise operation.A number can be used
          as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The second input to use in this bitwise operation.A number can be used
          as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of a Bitwise Or
          operation on the two
          inputs.

        """