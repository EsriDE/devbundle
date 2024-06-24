# Generated documentation for module arcpy.management


class CompressFileGeodatabaseData(object):
    """
    Compresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.
    """

    @property
    def description(self) -> str:
        return """

        CompressFileGeodatabaseData_management(in_data, lossless)

        Compresses all the contents in a geodatabase, all the contents in a
        feature dataset, or an individual stand-alone feature class or table.

     INPUTS:
      in_data (Workspace / Feature Dataset / Table View / Raster Layer / Geometric Network):
          The geodatabase, feature dataset, feature class, or table to compress.
      lossless (Boolean):
          Indicates whether lossless compression will be used.Lossless
          compression-Lossless compression will be used. This is the
          default.Non-lossless compression-Lossless compression will not be
          used.This parameter is ignored for pre-10.0 file geodatabases.

        """