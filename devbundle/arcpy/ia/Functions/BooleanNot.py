# Generated documentation for module arcpy.ia.Functions


class BooleanNot(object):
    """
    Performs a Boolean Not (complement) operation on the cell values of the input raster.
    """

    @property
    def description(self) -> str:
        return """

        BooleanNot_ia(in_raster_or_constant)

        Performs a Boolean Not (complement) operation on the cell values of
        the input raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input to use in this Boolean operation.To use a number as an input
          for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output cell values will be either 0 or 1.

        """