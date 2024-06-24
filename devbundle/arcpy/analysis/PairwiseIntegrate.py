# Generated documentation for module arcpy.analysis


class PairwiseIntegrate(object):
    """
    Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect.
    """

    @property
    def description(self) -> str:
        return """

        PairwiseIntegrate_analysis(in_features;in_features..., {cluster_tolerance})

        Analyzes the coordinate locations of feature vertices among features
        in one or more feature classes. Those that fall within a specified
        distance of one another are assumed to represent the same location and
        are assigned a common coordinate value (in other words, they are
        colocated). The tool also adds vertices where feature vertices are
        within the x,y tolerance of an edge and where line segments intersect.

     INPUTS:
      in_features (Value Table):
          The feature classes that will be integrated. When the distance between
          features is small in comparison to the tolerance, the vertices or
          points will be clustered (moved to be coincident).
      cluster_tolerance {Linear Unit}:
          The distance that determines the range in which feature vertices are
          made coincident. To minimize undesired movement of vertices, the x,y
          tolerance should be small. If no value is provided, the x,y tolerance
          from the first dataset in the list of inputs will be used.Changing
          this parameter's value may cause failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.

        """