# Generated documentation for module arcpy.management


class PolygonToLine(object):
    """
    Creates a feature class containing lines that are converted from polygon boundaries with or without considering neighboring polygons.
    """

    @property
    def description(self) -> str:
        return """

        PolygonToLine_management(in_features, out_feature_class, {neighbor_option})

        Creates a feature class containing lines that are converted from
        polygon boundaries with or without considering neighboring polygons.

     INPUTS:
      in_features (Feature Layer):
          The input features that must be polygon.
      neighbor_option {Boolean}:
          Specifies whether or not to identify and store polygon neighboring
          information.IDENTIFY_NEIGHBORS-Polygon neighboring relationship will
          be identified
          and stored in the output. If different segments of a polygon share
          boundary with different polygons, the boundary will be split such that
          each uniquely shared segment will become a line with its two
          neighboring polygon FIDs stored in the output. This is the
          default.IGNORE_NEIGHBORS-Polygon neighboring relationship will be
          ignored;
          every polygon boundary will become a line feature with its original
          polygon feature ID stored in the output.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class.

        """