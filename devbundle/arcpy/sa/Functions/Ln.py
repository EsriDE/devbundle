# Generated documentation for module arcpy.sa.Functions


class Ln(object):
    """
    Calculates the natural logarithm (base e) of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        Ln_sa(in_raster_or_constant)

        Calculates the natural logarithm (base e) of cells in a raster.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          Input values for which to find the natural logarithm (Ln).To use a
          number as an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the base e (natural) logarithm
          of the input
          values.

        """