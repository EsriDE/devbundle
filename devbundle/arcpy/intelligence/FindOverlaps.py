# Generated documentation for module arcpy.intelligence


class FindOverlaps(object):
    """
    Finds overlapping areas in a feature class and provides a count for the number of overlaps.
    """

    @property
    def description(self) -> str:
        return """

        FindOverlaps_intelligence(in_features, out_intersection, out_centroid, {group_field})

        Finds overlapping areas in a feature class and provides a count for
        the number of overlaps.

     INPUTS:
      in_features (Feature Layer):
          The input polygon features for which overlaps will be computed.
      group_field {Field}:
          The in_features group field.

     OUTPUTS:
      out_intersection (Feature Class):
          The output intersection areas.
      out_centroid (Feature Class):
          The output centroid locations of the out_intersection features.

        """