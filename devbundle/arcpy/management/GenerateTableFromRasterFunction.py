# Generated documentation for module arcpy.management


class GenerateTableFromRasterFunction(object):
    """
    Converts a raster function dataset to a table or feature class. The input raster function should be a raster function designed to output a table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTableFromRasterFunction_management(raster_function, out_table, {raster_function_arguments;raster_function_arguments...})

        Converts a raster function dataset to a table or feature class. The
        input raster function should be a raster function designed to output a
        table or feature class.

     INPUTS:
      raster_function (File / String):
          The function template or function JSON object that outputs a table or
          feature class.
      raster_function_arguments {Value Table}:
          The function arguments and their values to be set. Each raster
          function has its own arguments and values, which are listed in the
          dialog of the tool.

     OUTPUTS:
      out_table (Table):
          The path, file name, and type (extension) of the output table or
          feature class.

        """