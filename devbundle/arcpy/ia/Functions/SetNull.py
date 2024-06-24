# Generated documentation for module arcpy.ia.Functions


class SetNull(object):
    """
    Set Null sets identified cell locations to NoData based on a specified criteria. It returns NoData if a conditional evaluation is true, and returns the value specified by another raster if it is false.
    """

    @property
    def description(self) -> str:
        return """

        SetNull_ia(in_conditional_raster, in_false_raster_or_constant, {where_clause})

        Set Null sets identified cell locations to NoData based on a specified
        criteria. It returns NoData if a conditional evaluation is true, and
        returns the value specified by another raster if it is false.

     INPUTS:
      in_conditional_raster (Composite Geodataset):
          The input raster representing the true or false result of the desired
          condition.It can be of integer or floating point type.
      in_false_raster_or_constant (Composite Geodataset):
          The input whose values will be used as the output cell values if the
          condition is false.It can be an integer or a floating-point raster, or
          a constant value.
      where_clause {SQL Expression}:
          A logical expression that determines which of the input cells are to
          be true or false.The expression follows the general form of an SQL
          expression. An
          example of a where_clause is "VALUE > 100".

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.If the conditional evaluation is true, NoData is
          returned. If false,
          the value of the second input raster is returned.

        """