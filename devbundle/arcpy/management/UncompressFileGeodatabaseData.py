# Generated documentation for module arcpy.management


class UncompressFileGeodatabaseData(object):
    """
    Uncompresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.
    """

    @property
    def description(self) -> str:
        return """

        UncompressFileGeodatabaseData_management(in_data, {config_keyword})

        Uncompresses all the contents in a geodatabase, all the contents in a
        feature dataset, or an individual stand-alone feature class or table.

     INPUTS:
      in_data (Workspace / Feature Dataset / Table View / Raster Layer / Geometric Network):
          The geodatabase, feature dataset, feature class, or table to
          uncompress.
      config_keyword {String}:
          The configuration keyword defining how the data will store once
          uncompressed

        """