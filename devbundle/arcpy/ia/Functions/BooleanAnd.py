# Generated documentation for module arcpy.ia.Functions


class BooleanAnd(object):
    """
    Performs a Boolean And operation on the cell values of two input rasters.
    """

    @property
    def description(self) -> str:
        return """

        BooleanAnd_ia(in_raster_or_constant1, in_raster_or_constant2)

        Performs a Boolean And operation on the cell values of two input
        rasters.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The first input to use in this Boolean operation.A number can be used
          as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The second input to use in this Boolean operation.A number can be used
          as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output cell values will be either 0 or 1.

        """