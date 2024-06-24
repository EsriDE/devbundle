# Generated documentation for module arcpy.analysis


class TableSelect(object):
    """
    Selects table records matching a Structured Query Language (SQL) expression and writes them to an output table.
    """

    @property
    def description(self) -> str:
        return """

        TableSelect_analysis(in_table, out_table, {where_clause})

        Selects table records matching a Structured Query Language (SQL)
        expression and writes them to an output table.

     INPUTS:
      in_table (Table View / Raster Layer):
          The table containing records matching the specified expression that
          will be written to the output table.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records. For more
          information on SQL syntax, see SQL reference for elements used in
          query expressions.

     OUTPUTS:
      out_table (Table):
          The output table containing records from the input table that match
          the specified expression.

        """