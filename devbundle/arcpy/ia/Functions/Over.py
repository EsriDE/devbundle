# Generated documentation for module arcpy.ia.Functions


class Over(object):
    """
    For the cell values in the first input that are not 0, the output value will be that of the first input. Where the cell values are 0, the output will be that of the second input raster.
    """

    @property
    def description(self) -> str:
        return """

        Over_ia(in_raster_or_constant1, in_raster_or_constant2)

        For the cell values in the first input that are not 0, the output
        value will be that of the first input. Where the cell values are 0,
        the output will be that of the second input raster.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input for which cell values of 0 will be replaced with the value
          from the second input.A number can be used as an input for this
          parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input whose value will be assigned to the output raster cells
          where the first input value is 0.A number can be used as an input for
          this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.

        """