# Generated documentation for module arcpy.management


class CopyRows(object):
    """
    Copies the rows of a table to a different table.
    """

    @property
    def description(self) -> str:
        return """

        CopyRows_management(in_rows, out_table, {config_keyword})

        Copies the rows of a table to a different table.

     INPUTS:
      in_rows (Table View / Raster Layer):
          The input rows to be copied to a new table.
      config_keyword {String}:
          The default storage parameters for an enterprise geodatabase.

     OUTPUTS:
      out_table (Table):
          The table that will be created and to which rows from the input will
          be copied.If the output table is in a folder, include an extension
          such as .csv,
          .txt, or .dbf to make the table the specified format. If the output
          table is in a geodatabase, do not specify an extension.

        """