# Generated documentation for module arcpy.sa.Functions


class Int(object):
    """
    Converts each cell value of a raster to an integer by truncation.
    """

    @property
    def description(self) -> str:
        return """

        Int_sa(in_raster_or_constant)

        Converts each cell value of a raster to an integer by truncation.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster to be converted to integer.To use a number as an
          input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the input values converted to
          integers by
          truncation.

        """