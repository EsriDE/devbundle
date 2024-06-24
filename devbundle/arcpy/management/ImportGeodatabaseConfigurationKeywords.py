# Generated documentation for module arcpy.management


class ImportGeodatabaseConfigurationKeywords(object):
    """
    Defines data storage parameters for an enterprise geodatabase by importing a file containing configuration keywords, parameters, and values.
    """

    @property
    def description(self) -> str:
        return """

        ImportGeodatabaseConfigurationKeywords_management(input_database, in_file)

        Defines data storage parameters for an enterprise geodatabase by
        importing a file containing configuration keywords, parameters, and
        values.

     INPUTS:
      input_database (Workspace):
          The connection file for the enterprise geodatabase to which you want
          to import the configuration file. You must connect as the geodatabase
          administrator.
      in_file (File):
          The path to and name of the ASCII text file containing configuration
          keywords, parameters, and values to import.

        """