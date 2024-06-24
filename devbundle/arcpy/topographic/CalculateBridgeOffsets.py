# Generated documentation for module arcpy.topographic


class CalculateBridgeOffsets(object):
    """
    Calculates the offsets necessary to properly display bridges at a given location.
    """

    @property
    def description(self) -> str:
        return """

        CalculateBridgeOffsets_topographic(in_bridge_features, in_overpassing_features, reference_scale, {search_distance}, {expand}, {offset}, {min_length}, {bridge_subtype}, {overpassing_subtype})

        Calculates the offsets necessary to properly display bridges at a
        given location.

     INPUTS:
      in_bridge_features (Layer):
          The feature layer that contains bridge features for which symbol
          offsets will be updated. Symbolize the bridge features layer with
          proper bridge features and enable attribute-driven symbology on it.
      in_overpassing_features (Layer):
          The feature layer that contains the features overpassing the bridges.
      reference_scale (Long):
          The scale at which symbols appear at their intended size.
      search_distance {Linear Unit}:
          The distance, calculated in map units, by which this tool will buffer
          point bridge features when identifying the overpassing features. This
          parameter is only available for point bridges. The default is 0
          meters.
      expand {Boolean}:
          Specifies whether marker layers on overpassing symbols will be
          included when analyzing widths.EXPAND-Marker layers on overpassing
          symbols will be included when
          analyzing widths.NO_EXPAND-Marker layers on overpassing symbols will
          not be included.
          This is the default.
      offset {Linear Unit}:
          An offset added to the bridge width. The default is 0 points.
      min_length {Linear Unit}:
          The minimum length of a line bridge. The default is 1.35
          millimeters.If the length of the bridge is less than the minimum
          length, it will
          be expanded to minimum length.
      bridge_subtype {String}:
          The subtype of the feature class from the in_bridge_features parameter
          that will be modified by this operation.
      overpassing_subtype {String}:
          The subtype of the feature class in the in_overpassing_features
          parameter that will be used in this operation.

        """