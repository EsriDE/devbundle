# Generated documentation for module arcpy.edit


class Snap(object):
    """
    Moves points or vertices to coincide exactly with the vertices, edges, or end points of other features. Snapping rules can be specified to control whether the input vertices are snapped to the nearest vertex, edge, or endpoint within a specified distance.
    """

    @property
    def description(self) -> str:
        return """

        Snap_edit(in_features, snap_environment;snap_environment...)

        Moves points or vertices to coincide exactly with the vertices, edges,
        or end points of other features. Snapping rules can be specified to
        control whether the input vertices are snapped to the nearest vertex,
        edge, or endpoint within a specified distance.

     INPUTS:
      in_features (Feature Layer):
          The input features with the vertices that will be snapped to the
          vertices, edges, or end points of other features. The input features
          can be points, multipoints, lines, or polygons.
      snap_environment (Value Table):
          The feature classes or feature layers containing the features to snap
          to.The snapping environment components are as follows:Features-The
          features that the input features' vertices will be
          snapped to. These features can be points, multipoints, lines, or
          polygons.Type-The type of feature part that the input features'
          vertices can be
          snapped to.Distance-The distance within which the input features'
          vertices will
          be snapped to the nearest end point, vertex, or edge.Available
          snapping types are as follows:END-Input feature vertices will be
          snapped to feature
          ends.VERTEX-Input feature vertices will be snapped to feature
          vertices.EDGE-Input feature vertices will be snapped to feature
          edges.If a distance is used without a unit (for example, 10 instead of
          10
          meters), the linear or angular unit from the input feature's
          coordinate system will be used as the default. If the input features
          have a projected coordinate system, its linear unit will be used.

        """