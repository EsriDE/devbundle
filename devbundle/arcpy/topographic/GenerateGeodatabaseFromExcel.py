# Generated documentation for module arcpy.topographic


class GenerateGeodatabaseFromExcel(object):
    """
    Creates a geodatabase from the contents of a Microsoft Excel file (.xls or .xlsx).
    """

    @property
    def description(self) -> str:
        return """

        GenerateGeodatabaseFromExcel_topographic(in_excel_file, out_geodatabase)

        Creates a geodatabase from the contents of a Microsoft Excel file
        (.xls or .xlsx).

     INPUTS:
      in_excel_file (File):
          The Excel file that will be used to generate the geodatabase.
      out_geodatabase (Workspace):
          The geodatabase that will be generated from the Excel file.

        """