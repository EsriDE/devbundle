# Generated documentation for module arcpy.conversion


class RasterToGeodatabase(object):
    """
    Loads raster datasets into a geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        RasterToGeodatabase_conversion(Input_Rasters;Input_Rasters..., Output_Geodatabase, {Configuration_Keyword})

        Loads raster datasets into a geodatabase.

     INPUTS:
      Input_Rasters (Raster Dataset / Raster Layer):
          The input raster datasets.
      Output_Geodatabase (Workspace):
          The output or destination geodatabase.
      Configuration_Keyword {String}:
          The storage parameters (configuration) for a geodatabase.
          Configuration keywords are set up by your database administrator.

        """