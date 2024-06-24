# Generated documentation for module arcpy.aviation


class GenerateSummaryTableData(object):
    """
    Collects information from a source cartographic feature class and related tables in an aviation charting database (AIS) and outputs the resulting information to a stand-alone table.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSummaryTableData_aviation(target_geodatabase, in_preferences;in_preferences..., in_charts_table)

        Collects information from a source cartographic feature class and
        related tables in an aviation charting database (AIS) and outputs the
        resulting information to a stand-alone table.

     INPUTS:
      target_geodatabase (Workspace):
          The Aviation charting schema geodatabase.
      in_preferences (String):
          The preferences stored in the database that control how, and for which
          charts, summary table information will be generated.
      in_charts_table (Table View):
          The table or polygon feature class that defines chart areas for
          tabulation. If a table view or layer view is input, its definition
          query will be honored.

        """