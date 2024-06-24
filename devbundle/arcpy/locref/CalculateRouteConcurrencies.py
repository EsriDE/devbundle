# Generated documentation for module arcpy.locref


class CalculateRouteConcurrencies(object):
    """
    Calculates and reports concurrent route sections in an LRS Network.
    """

    @property
    def description(self) -> str:
        return """

        CalculateRouteConcurrencies_locref(in_route_features, out_dataset, {tvd}, {find_dominance}, {include_geometry})

        Calculates and reports concurrent route sections in an LRS Network.

     INPUTS:
      in_route_features (Feature Layer):
          The LRS Network feature class in which route concurrencies will be
          calculated.
      tvd {Date}:
          The temporal view date for the network, if one is specified. Leaving
          this field blank shows all time.
      find_dominance {Boolean}:
          Specifies whether configured route dominance rules will be used to set
          dominance.FIND_DOMINANCE-Configured route dominance rules will be used
          to
          determine the dominant route in each concurrent section. This is the
          default.NO_FIND_DOMINANCE-Configured route dominance rules will not be
          used to
          determine the dominant route in each concurrent section.
      include_geometry {Boolean}:
          Specifies whether geometry will be included in the output
          dataset.EXCLUDE_GEOMETRY-Geometry will not be included in the output
          dataset.
          This is the default.INCLUDE_GEOMETRY-Geometry will be included in the
          output dataset.

     OUTPUTS:
      out_dataset (Table):
          The feature class or table to which the calculated results will be
          posted.

        """