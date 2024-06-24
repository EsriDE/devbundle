# Generated documentation for module arcpy.topographic


class RemoveCutbackVertices(object):
    """
    Removes unwanted cutbacks from polyline and polygon features.
    """

    @property
    def description(self) -> str:
        return """

        RemoveCutbackVertices_topographic(in_features, minimum_angle, {removal_method}, {skip_coincident_vertices})

        Removes unwanted cutbacks from polyline and polygon features.

     INPUTS:
      in_features (Feature Layer):
          The polyline or polygon feature class from which cutback vertices will
          be removed. This feature class (or layer) will be modified.
      minimum_angle (Double):
          The minimum angle threshold value in degrees. The angle value should
          be within the range of 0-180. If the angle formed by a vertex and its
          two neighboring points is smaller than the specified minimum angle,
          the vertex is a candidate for cutback removal.
      removal_method {String}:
          Specifies whether cutbacks will be removed sequentially (individually)
          or all at once.SEQUENTIAL-Cutbacks will be removed sequentially for a
          feature. After
          a cutback is removed, the change in geometry is considered when
          determining cutbacks to the remaining vertices of a feature. This is
          the default.ALL-Cutbacks will be removed for all vertices at once.
      skip_coincident_vertices {Boolean}:
          Specifies whether cutback vertices will be removed when the vertex is
          snapped to another feature in the same feature
          class.SKIP_COINCIDENT-Cutback vertices with angles less than the
          minimum_angle value will not be removed from the feature geometry if
          they are snapped to other features.REMOVE_COINCIDENT-Cutback vertices
          will be removed without considering
          whether they are snapped to other features. This is the default.

        """