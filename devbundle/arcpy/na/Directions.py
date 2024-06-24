# Generated documentation for module arcpy.na


class Directions(object):
    """
    Generates turn-by-turn directions from a network analysis layer with routes. The directions can be written to a file in text, XML, or HTML format. If you provide an appropriate style sheet, the directions can be written to any other file format.
    """

    @property
    def description(self) -> str:
        return """

        Directions_na(in_network_analysis_layer, file_type, out_directions_file, report_units, {report_time}, {time_attribute}, {language}, {style_name}, {stylesheet})

        Generates turn-by-turn directions from a network analysis layer with
        routes. The directions can be written to a file in text, XML, or HTML
        format. If you provide an appropriate style sheet, the directions can
        be written to any other file format.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer for which directions will be generated.
          Directions can be generated only for route, closest facility, and
          vehicle routing problem network analysis layers. This tool does
          not support last mile delivery analysis layers
          even though this layer type supports directions.
      file_type (String):
          Specifies the format that will be used for the output directions file.
          This parameter is ignored if the style sheet parameter has a
          value.XML-The output directions file will be generated as an XML file.
          Apart
          from direction strings and the length and time information for the
          routes, the file will also contain information about the maneuver type
          and the turn angle for each direction.TEXT-The output directions file
          will be generated as a simple TXT file
          containing the direction strings, the length and, optionally, the time
          information for the routes.HTML-The output directions file will be
          generated as an HTML file
          containing the direction strings, the length and, optionally, the time
          information for the routes.
      report_units (String):
          Specifies the linear units that will be used in the directions file.
          For example, even if the impedance attribute has units of meters, you
          can show directions in miles.Feet-The linear units will be
          feet.Yards-The linear units will be
          yards.Miles-The linear units will be miles.Meters-The linear units
          will be meters.Kilometers-The linear units will be
          kilometers.NauticalMiles-The linear units will be nautical miles
      report_time {Boolean}:
          Specifies whether travel time will be reported in the directions
          file.NO_REPORT_TIME-Travel time will not be reported in the directions
          file.REPORT_TIME-Travel time will be reported in the directions file.
          This
          is the default.
      time_attribute {String}:
          The time-based cost attribute that will be used to provide travel
          times in the directions. The cost attribute must exist on the network
          dataset used by the input network analysis layer.
      language {String}:
          The language that will be used for driving directions.Use a two- or
          five-character language code representing one of the
          available languages for directions generation for this parameter
          value. In Python, you can retrieve a list of available language codes
          using the ListDirectionsLanguages function.
      style_name {String}:
          Specifies the formatting style that will be used for directions.NA
          Desktop-Printable turn-by-turn directions will be used.NA
          Navigation-Turn-by-turn directions designed for an in-vehicle
          navigation device will be used.NA Campus-Turn-by-turn walking
          directions, which are designed for
          pedestrian routes, will be used.
      stylesheet {File}:
          The style sheet that will be used for generating a formatted output
          file type (such as a PDF, Word, or HTML). The suffix of the file in
          the output directions file parameter must match the file type that the
          style sheet generates. The tool overrides the output file type
          parameter if this parameter contains a value.To create custom HTML and
          text style sheets, copy and edit the style
          sheets from Network Analyst. The style sheets are available in the
          <ArcGIS installation
          directory>\Pro\Resources\NetworkAnalyst\Directions\Styles directory.
          The HTML style sheet is Dir2PHTML.xsl, and the text style sheet is
          Dir2PlainText.xsl.

     OUTPUTS:
      out_directions_file (File):
          If you provide a style sheet for the stylesheet parameter, ensure that
          the file suffix for out_directions_file matches the file type the
          style sheet produces.

        """