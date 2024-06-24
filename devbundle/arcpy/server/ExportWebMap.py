# Generated documentation for module arcpy.server


class ExportWebMap(object):
    """
    Returns a printable page layout or basic map of a specified area of interest based on the state of a web app (for example, included services, layer visibility settings, and client-side graphics).
    """

    @property
    def description(self) -> str:
        return """

        ExportWebMap_server(Web_Map_as_JSON, Output_File, {Format}, {Layout_Templates_Folder}, {Layout_Template}, {Layout_Item_ID}, {Report_Template}, {Report_Item_ID})

        Returns a printable page layout or basic map of a specified area of
        interest based on the state of a web app (for example, included
        services, layer visibility settings, and client-side graphics).

     INPUTS:
      Web_Map_as_JSON (String):
          A JSON representation of the state of the map to be exported as it
          appears in the web app. See the ExportWebMap specification to
          understand how to format this text. ArcGIS API for JavaScript allows
          you to get this JSON string from the map.
      Format {String}:
          Specifies the format in which the map image for printing will be
          delivered.PNG8-8-bit Portable Network Graphics (PNG8) will be used.
          This is the
          default.PDF-Portable Document Format (PDF) will be used.PNG32-32-bit
          Portable Network Graphics (PNG32) will be used.JPG-Joint Photographic
          Experts Group (JPG) will be used.GIF-Graphics Interchange Format
          (GIF) will be used.EPS-Encapsulated PostScript (EPS) will be
          used.SVG-Scalable Vector Graphics (SVG) will be used.SVGZ-Compressed
          Scalable Vector Graphics (SVGZ) will be used.AIX-Adobe Illustrator
          Exchange (AIX) will be used.TIFF-Tag Image File Format (TIFF) will be
          used.The background of the output file is always opaque.
      Layout_Templates_Folder {Folder}:
          The full path to the folder containing layout or report pages (.pagx,
          .rptx, and .rptt files) to be used as templates. The default location
          is <install_directory>\Resources\ArcToolBox\Templates\ExportWebMapTemp
          lates.
      Layout_Template {String}:
          The name of a template from the list or the keyword MAP_ONLY. When
          MAP_ONLY is used or an empty string is passed in, the output map will
          not contain any page layout elements such as title, legend, or scale
          bar.
      Layout_Item_ID {String}:
          The portal ID (in JSON format) of the layout item that will be used
          for templates. Use the format: {"id": "<portal-id>"}. When a value is
          provided, this parameter takes precedence over the Layout_Template
          parameter.
      Report_Template {String}:
          The name of the report template.When this parameter is provided, the
          Format parameter must be set to
          PDF. When this parameter is unspecified, the output file will not
          contain any reports.
      Report_Item_ID {String}:
          The portal ID (in JSON format) of the report item that will be used
          for templates. Use the format: {"id": "<portal-id>"}. When a value is
          provided, this parameter takes precedence over the Report_Template
          parameter.

     OUTPUTS:
      Output_File (File):
          The output file name. The extension of the file depends on the Format
          parameter value.

        """