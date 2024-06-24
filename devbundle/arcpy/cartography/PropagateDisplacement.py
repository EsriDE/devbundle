# Generated documentation for module arcpy.cartography


class PropagateDisplacement(object):
    """
    Propagates the displacement resulting from road adjustment in the Resolve Road Conflicts and Merge Divided Roads tools to adjacent features to reestablish spatial relationships.
    """

    @property
    def description(self) -> str:
        return """

        PropagateDisplacement_cartography(in_features, displacement_features, adjustment_style)

        Propagates the displacement resulting from road adjustment in the
        Resolve Road Conflicts and Merge Divided Roads tools to adjacent
        features to reestablish spatial relationships.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer containing features that may be in conflict.
          May be point, line, or polygon.
      displacement_features (Feature Layer):
          The displacement polygon features created by the Resolve Road
          Conflicts or the Merge Divided Roads tools that contain the degree and
          direction of road displacement that took place. These polygons dictate
          the amount of displacement that will be propagated to the input
          features.
      adjustment_style (String):
          Defines the type of adjustment that will be used when displacing input
          features.AUTO-The tool will decide for each input feature whether a
          SOLID or an
          ELASTIC adjustment is most appropriate. In general, features with
          orthogonal shapes will have SOLID adjustment applied, while
          organically shaped features will have ELASTIC adjustment applied. This
          is the default.SOLID-The feature will be translated. All vertices will
          move the same
          distance and direction. Topological errors may be introduced. This
          option is most useful when input features have regular geometric
          shapes.ELASTIC-The vertices of the feature may be moved independently
          to best
          fit the feature to the road network. The shape of the feature may be
          modified slightly. Topological errors are less likely to be
          introduced. This option only applies to line and polygon input
          features. This option is most useful for organically shaped input
          features.

        """