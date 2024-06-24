# Generated documentation for module arcpy.na


class IncreaseMaximumEdges(object):
    """
    Increases the maximum number of edges per turn in a turn feature class.
    """

    @property
    def description(self) -> str:
        return """

        IncreaseMaximumEdges_na(in_turn_features, maximum_edges)

        Increases the maximum number of edges per turn in a turn feature
        class.

     INPUTS:
      in_turn_features (Feature Layer):
          The turn feature class that is having its maximum number of edges
          raised.
      maximum_edges (Long):
          The new maximum number of edges in the input turn feature class. The
          value must be at least one higher than the existing maximum number of
          edges and cannot be greater than 50.

        """