# Generated documentation for module arcpy.management


class GetCount(object):
    """
    Returns the total number of rows for a table.
    """

    @property
    def description(self) -> str:
        return """

        GetCount_management(in_rows)

        Returns the total number of rows for a table.

     INPUTS:
      in_rows (Table View / Raster Layer):
          The input table view or raster layer. If a selection is defined on the
          input, the count of the selected rows will be returned.

        """