# Generated documentation for module arcpy.management


class MakeTableView(object):
    """
    Creates a table view from an input table or feature class. The table view that is created is temporary and will not persist after the session ends unless the document is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeTableView_management(in_table, out_view, {where_clause}, {workspace}, {field_info})

        Creates a table view from an input table or feature class. The table
        view that is created is temporary and will not persist after the
        session ends unless the document is saved.

     INPUTS:
      in_table (Table View / Raster Layer):
          The input table or feature class.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more
          information on SQL syntax see the help topic SQL reference for query
          expressions used in ArcGIS.
      workspace {Workspace}:
          This parameter is not used.
      field_info {Field Info}:
          The fields from the input table that will be included in the output
          layer. You can remove input fields by setting them to not visible.
          Renaming fields and the use of split policies are not supported.

     OUTPUTS:
      out_view (Table View / Raster Layer):
          The name of the table view to be created.

        """