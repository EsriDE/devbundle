# Generated documentation for module arcpy.management


class GenerateSchemaReport(object):
    """
    Generates an Excel, JSON, PDF, or HTML representation of the geodatabase schema. These formats are output to a target destination folder.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSchemaReport_management(in_dataset, out_location, name, formats;formats...)

        Generates an Excel, JSON, PDF, or HTML representation of the
        geodatabase schema. These formats are output to a target destination
        folder.

     INPUTS:
      in_dataset (Workspace / Feature Dataset / Table View):
          The workspace, feature dataset, feature layer, or table view that will
          be used to generate the schema report.
      out_location (Folder):
          The folder where the report will be created.
      name (String):
          The name of the file outputs.
      formats (String):
          Specifies the file types that will be included in the output
          folder.JSON-The output folder will include a .json file.PDF-The output
          folder
          will include a .pdf file.HTML-The output folder will include an .html
          file.XLSX-The output folder will include an Excel .xlsx file.

        """