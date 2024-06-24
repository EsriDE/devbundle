# Generated documentation for module arcpy.sa.Functions


class ATan2(object):
    """
    Calculates the inverse tangent (based on x,y) of cells in a raster.
    """

    @property
    def description(self) -> str:
        return """

        ATan2_sa(in_raster_or_constant1, in_raster_or_constant2)

        Calculates the inverse tangent (based on x,y) of cells in a raster.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input that specifies the numerator, or y value, to use when
          calculating the inverse tangent.A number can be used as an input for
          this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input that specifies the denominator, or x value, to use when
          calculating the inverse tangent.A number can be used as an input for
          this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values are the inverse tangent angle of the
          input values.

        """