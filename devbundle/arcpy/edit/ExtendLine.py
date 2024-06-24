# Generated documentation for module arcpy.edit


class ExtendLine(object):
    """
    Extends line segments to the first intersecting feature within a specified distance. If no intersecting feature is within the specified distance, the line segment will not be extended. Tool use is intended for quality control tasks such as cleaning up topology errors in features that were digitized without having set proper snapping environments.
    """

    @property
    def description(self) -> str:
        return """

        ExtendLine_edit(in_features, {length}, {extend_to})

        Extends line segments to the first intersecting feature within a
        specified distance. If no intersecting feature is within the specified
        distance, the line segment will not be extended. Tool use is intended
        for quality control tasks such as cleaning up topology errors in
        features that were digitized without having set proper snapping
        environments.

     INPUTS:
      in_features (Feature Layer):
          The line input features to be extended.
      length {Linear Unit}:
          The maximum distance a line segment can be extended to an intersecting
          feature.
      extend_to {Boolean}:
          Specifies whether line segments can be extended to other extended line
          segments within the specified extend length.EXTENSION-Line segments
          can be extended to other extended line
          segments as well as existing line features. This is the
          default.FEATURE-Line segments can only be extended to existing line
          features.

        """