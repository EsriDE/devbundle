# Generated documentation for module arcpy.topographic


class RemoveSmallLines(object):
    """
    Removes lines that are shorter than a specified minimum length and do not connect to other features on one end.
    """

    @property
    def description(self) -> str:
        return """

        RemoveSmallLines_topographic(in_features, minimum_length, {maximum_angle}, {in_intersecting_features;in_intersecting_features...}, {recursive}, {split_input_lines})

        Removes lines that are shorter than a specified minimum length and do
        not connect to other features on one end.

     INPUTS:
      in_features (Feature Layer):
          The features that will have small lines removed.
      minimum_length (Linear Unit):
          The minimum length for input lines. Features shorter than this
          distance will be removed.
      maximum_angle {Long}:
          Any line below the minimum length that is within the defined angle of
          a consecutive line segment will be kept. The angle value must be
          within the range of 0-180.
      in_intersecting_features {Feature Layer}:
          Additional intersecting features that the input features can be
          compared to when determining whether the feature is a small line.
      recursive {Boolean}:
          Specifies whether small lines on the line features will be
          removed.NON_RECURSIVE-All the small lines on line features will be
          removed.
          The remaining lines will not be analyzed to determine whether they are
          small lines. This is the default.RECURSIVE-The small lines will be
          removed from the line features and
          the remaining lines will be analyzed to determine whether they are
          small lines. If they do not meet the minimum_length value, they will
          be identified as small lines and removed.
      split_input_lines {Boolean}:
          Specifies whether the input line features will be split at all
          intersections before determining the small lines to remove.SPLIT-All
          lines in the input feature class will be split at
          intersections to ensure topological integrity. The length of the split
          features, not the original feature geometries, will be used when
          applying the minimum length value to determine small lines. This is
          the default.NO_SPLIT-The lines will not be split before determining
          the lines to
          remove. The length of the input feature geometries will be used when
          applying the minimum length value to determine small lines.

        """