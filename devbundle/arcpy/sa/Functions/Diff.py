# Generated documentation for module arcpy.sa.Functions


class Diff(object):
    """
    Determines which values from the first input are logically different from the values of the second input on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        Diff_sa(in_raster_or_constant1, in_raster_or_constant2)

        Determines which values from the first input are logically different
        from the values of the second input on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input to which the second input will be compared.A number can be
          used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input to which the first input will be compared.A number can be
          used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The values in the output will be either 0 if the two
          input values are
          the same, or the first input value if they are not.

        """