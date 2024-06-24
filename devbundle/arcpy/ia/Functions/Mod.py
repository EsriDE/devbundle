# Generated documentation for module arcpy.ia.Functions


class Mod(object):
    """
    Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Mod_ia(in_raster_or_constant1, in_raster_or_constant2)

        Finds the remainder (modulo) of the first raster when divided by the
        second raster on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The numerator input.A number can be used as an input for this
          parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The denominator input.A number can be used as an input for this
          parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the remainder of the division of
          the values in the
          first input by the second input.

        """