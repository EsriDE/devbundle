# Generated documentation for module arcpy.management


class ExportGeodatabaseConfigurationKeywords(object):
    """
    Exports the configuration keywords, parameters, and values from the specified enterprise geodatabase to an editable file. Change parameter values or add custom configuration keywords to the file and use the Import Geodatabase Configuration Keywords tool to import the changes to the geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        ExportGeodatabaseConfigurationKeywords_management(input_database, out_file)

        Exports the configuration keywords, parameters, and values from the
        specified enterprise geodatabase to an editable file. Change parameter
        values or add custom configuration keywords to the file and use the
        Import Geodatabase Configuration Keywords tool to import the changes
        to the geodatabase.

     INPUTS:
      input_database (Workspace):
          The connection file for the enterprise geodatabase from which you want
          to export configuration keywords, parameters, and values. You must
          connect as the geodatabase administrator.

     OUTPUTS:
      out_file (File):
          The full path to and name of the ASCII text file to be created. The
          file will contain all the configuration keywords, parameters, and
          values from the enterprise geodatabase's DBTUNE (or SDE_DBTUNE) system
          table.

        """