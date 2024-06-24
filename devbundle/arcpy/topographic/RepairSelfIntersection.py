# Generated documentation for module arcpy.topographic


class RepairSelfIntersection(object):
    """
    Repairs self-intersecting line or polygon features. The portion between the feature and the intersection points are either deleted or split into a new feature.
    """

    @property
    def description(self) -> str:
        return """

        RepairSelfIntersection_topographic(in_features, repair_type, {max_length}, {repair_at_end_point})

        Repairs self-intersecting line or polygon features. The portion
        between the feature and the intersection points are either deleted or
        split into a new feature.

     INPUTS:
      in_features (Feature Layer):
          The polyline or polygon feature class with the self-intersections that
          will be repaired.
      repair_type (String):
          Specifies whether self-intersections will be deleted or
          split.DELETE-Self-intersections will be deleted. This is the
          default.SPLIT-Self-intersections will be split at the intersection
          point and
          retained.
      max_length {Linear Unit}:
          The maximum length of the segment between the points of self-
          intersection. Only segments shorter than the specified maximum length
          will be removed.
      repair_at_end_point {Boolean}:
          Specifies whether self-intersections with an end point that snaps to
          itself will be removed.REPAIR_ENDS-Self-intersections with an end
          point that snaps to itself
          will be removed.IGNORE_ENDS-Self-intersections with an end point that
          snaps to itself
          (such as a cul-de-sac) will not be removed. This is the default.

        """