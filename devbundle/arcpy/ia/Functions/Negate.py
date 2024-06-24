# Generated documentation for module arcpy.ia.Functions


class Negate(object):
    """
    Changes the sign (multiplies by -1) of the cell values of the input raster on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Negate_ia(in_raster_or_constant)

        Changes the sign (multiplies by -1) of the cell values of the input
        raster on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster to be negated (multiplied by -1).To use a number as
          an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the input values negated
          (multiplied by -1).

        """