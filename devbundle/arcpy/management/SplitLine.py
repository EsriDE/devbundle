# Generated documentation for module arcpy.management


class SplitLine(object):
    """
    Creates a polyline feature class by splitting input lines or polygons at their vertices.
    """

    @property
    def description(self) -> str:
        return """

        SplitLine_management(in_features, out_feature_class)

        Creates a polyline feature class by splitting input lines or polygons
        at their vertices.

     INPUTS:
      in_features (Feature Layer):
          The input line or polygon features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class.

        """