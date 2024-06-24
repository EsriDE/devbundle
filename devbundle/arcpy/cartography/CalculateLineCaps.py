# Generated documentation for module arcpy.cartography


class CalculateLineCaps(object):
    """
    Modifies the cap type for stroke symbol layers in the line symbols of the input layer.
    """

    @property
    def description(self) -> str:
        return """

        CalculateLineCaps_cartography(in_features, {cap_type}, {dangle_option})

        Modifies the cap type for stroke symbol layers in the line symbols of
        the input layer.

     INPUTS:
      in_features (Layer):
          The input feature layer containing line symbols. Stroke symbol
          layers must have theproperty connected to a single attribute field
          with no expression applied. The values in this field are updated by
          this tool. Cap Type
      cap_type {String}:
          Specifies how the ends of stroke symbol layers will be drawn. The
          default cap type of strokes is round; the symbol is terminated with a
          semicircle of radius equal to stroke width centered at the line
          endpoint.BUTT-The stroke symbol will end exactly where the line
          geometry ends.
          This is the default.SQUARE-The stroke symbol will end with closed,
          square caps that extend
          past the endpoint of the line by half the symbol width.
      dangle_option {String}:
          Specifies how line caps will be calculated for adjoining line features
          that share an endpoint but are drawn with different
          symbology.CASED_LINE_DANGLE-The cap style will be modified for
          dangling lines
          (those not connected at their endpoints to another line), as well as
          for lines where a cased-line symbol is joined at the endpoint of a
          single-stroke layer line symbol. This is the default.TRUE_DANGLE-The
          cap style will be modified only for endpoints that are
          not connected to another feature.

        """