# Generated documentation for module arcpy.management


class ConvertRasterFunctionTemplate(object):
    """
    Converts a raster function template between formats (rft.xml, json, and binary).
    """

    @property
    def description(self) -> str:
        return """

        ConvertRasterFunctionTemplate_management(in_raster_function_template, out_raster_function_template_file, {format})

        Converts a raster function template between formats (rft.xml, json,
        and binary).

     INPUTS:
      in_raster_function_template (File / String):
          The input raster function template file. The input template file can
          be XML, JSON, or binary format.
      format {String}:
          The output function template file format.XML-XML output
          format.JSON-JSON output format. This is the
          default.BINARY-Binary output format.

     OUTPUTS:
      out_raster_function_template_file (File):
          The output raster function template file path and file name.

        """