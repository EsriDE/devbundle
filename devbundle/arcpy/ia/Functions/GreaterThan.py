# Generated documentation for module arcpy.ia.Functions


class GreaterThan(object):
    """
    Performs a Relational greater-than operation on two inputs on a cell- by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        GreaterThan_ia(in_raster_or_constant1, in_raster_or_constant2)

        Performs a Relational greater-than operation on two inputs on a cell-
        by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input being tested to determine if it is greater than the second
          input.A number can be used as an input for this parameter, provided a
          raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input against which the first input is tested to be greater than.A
          number can be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output cell values will be either integer 0 or
          1, or NoData if any
          input cell value is NoData.

        """