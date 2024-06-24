# Generated documentation for module arcpy.management


class MatchLayerSymbologyToAStyle(object):
    """
    Creates unique value symbology for the input layer based on the input field or expression by matching input field or expression strings to symbol names from the input style.
    """

    @property
    def description(self) -> str:
        return """

        MatchLayerSymbologyToAStyle_management(in_layer, match_values, in_style)

        Creates unique value symbology for the input layer based on the input
        field or expression by matching input field or expression strings to
        symbol names from the input style.

     INPUTS:
      in_layer (Feature Layer):
          The input layer or layer file to which matched symbols are applied as
          unique values symbol classes. The input layer can contain point, line,
          polygon, multipoint, or multipatch symbology. Existing symbology on
          the layer is overwritten.
      match_values (Calculator Expression):
          The field or expression on which the input layer is symbolized. The
          field values or resultant expression values are matched to symbol
          names in the specified style to assign symbols to the resulting symbol
          classes.
      in_style (String):
          The style containing symbols with names matching the field or
          expression values.

        """