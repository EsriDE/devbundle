# Generated documentation for module arcpy.ia.Functions


class BitwiseNot(object):
    """
    Performs a Bitwise Not (complement) operation on the binary value of an input raster.
    """

    @property
    def description(self) -> str:
        return """

        BitwiseNot_ia(in_raster_or_constant)

        Performs a Bitwise Not (complement) operation on the binary value of
        an input raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster on which to perform the Bitwise Not (complement)
          operation.A number can be used as an input for this parameter,
          provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of a Bitwise Not
          operation on the
          input.

        """