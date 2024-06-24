# Generated documentation for module arcpy.sa.Functions


class Test(object):
    """
    Performs a Boolean evaluation of the input raster using a logical expression.
    """

    @property
    def description(self) -> str:
        return """

        Test_sa(in_raster, where_clause)

        Performs a Boolean evaluation of the input raster using a logical
        expression.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster on which the Boolean evaluation is performed, based
          on a logical expression.
      where_clause (SQL Expression):
          The logical expression that will determine which input cells will
          return a value of true (1) and which will be false (0).The expression
          follows the general form of an SQL expression. An
          example of a where_clause is "VALUE > 100".

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output cell values will be either 0 or 1.

        """