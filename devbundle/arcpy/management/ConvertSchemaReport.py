# Generated documentation for module arcpy.management


class ConvertSchemaReport(object):
    """
    Converts a JSON or XLSX formatted schema report to another schema report format or to an XML workspace document that can be used to create a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ConvertSchemaReport_management(schema_report, out_location, name, formats;formats...)

        Converts a JSON or XLSX formatted schema report to another schema
        report format or to an XML workspace document that can be used to
        create a geodatabase.

     INPUTS:
      schema_report (File):
          The JSON or XLSX schema report that will be converted.
      out_location (Folder):
          The folder where the output files will be placed
      name (String):
          The name of the file outputs.
      formats (String):
          Specifies the file types that will be included in the output
          folder.JSON-The output folder will include a .json file.PDF-The output
          folder
          will include a .pdf file.HTML-The output folder will include an .html
          file.XLSX-The output folder will include an Excel .xlsx file.XML-The
          output folder will include an .xml file.

        """