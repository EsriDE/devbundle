# Generated documentation for module arcpy.topographic


class GenerateExcelFromGeodatabase(object):
    """
    Creates a Microsoft Excel file (.xls or .xlsx) from the contents of a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        GenerateExcelFromGeodatabase_topographic(in_geodatabase, out_excel_file)

        Creates a Microsoft Excel file (.xls or .xlsx) from the contents of a
        geodatabase.

     INPUTS:
      in_geodatabase (Workspace):
          The geodatabase that will be used to create the Excel spreadsheet.

     OUTPUTS:
      out_excel_file (File):
          The Excel file that will be created from the geodatabase.

        """