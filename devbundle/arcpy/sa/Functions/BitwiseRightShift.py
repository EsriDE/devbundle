# Generated documentation for module arcpy.sa.Functions


class BitwiseRightShift(object):
    """
    Performs a Bitwise Right Shift operation on the binary values of two input rasters.
    """

    @property
    def description(self) -> str:
        return """

        BitwiseRightShift_sa(in_raster_or_constant1, in_raster_or_constant2)

        Performs a Bitwise Right Shift operation on the binary values of two
        input rasters.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input on which to perform the shift.A number can be used as an
          input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input defining the number of positions to shift the bits.A number
          can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of a Bitwise Right
          Shift operation on
          the inputs.

        """