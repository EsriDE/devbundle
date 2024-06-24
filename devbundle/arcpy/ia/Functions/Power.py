# Generated documentation for module arcpy.ia.Functions


class Power(object):
    """
    Raises the cell values in a raster to the power of the values found in another raster.
    """

    @property
    def description(self) -> str:
        return """

        Power_ia(in_raster_or_constant1, in_raster_or_constant2)

        Raises the cell values in a raster to the power of the values found in
        another raster.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input values to be raised to the power defined by the second
          input.A number can be used as an input for this parameter, provided a
          raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input that determines the power the values in the first input will
          be raised to.A number can be used as an input for this parameter,
          provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of raising the values
          in the first
          input to the power of the values in the second input.

        """