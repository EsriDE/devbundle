# Generated documentation for module arcpy.sa.Functions


class ExtractByAttributes(object):
    """
    Extracts the cells of a raster based on a logical query.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByAttributes_sa(in_raster, where_clause)

        Extracts the cells of a raster based on a logical query.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      where_clause (SQL Expression):
          A logical expression that selects a subset of raster cells.The
          expression follows the general form of an SQL expression. An
          example of a where_clause is "VALUE > 100".

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """