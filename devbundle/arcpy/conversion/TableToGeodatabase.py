# Generated documentation for module arcpy.conversion


class TableToGeodatabase(object):
    """
    Converts one or more tables to geodatabase tables in an output geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        TableToGeodatabase_conversion(Input_Table;Input_Table..., Output_Geodatabase)

        Converts one or more tables to geodatabase tables in an output
        geodatabase.

     INPUTS:
      Input_Table (Table View):
          The list of tables that will be converted to geodatabase tables. Input
          tables can be INFO, dBASE, OLE DB, geodatabase tables, or table views.
      Output_Geodatabase (Workspace):
          The destination geodatabase where the tables will be placed.

        """