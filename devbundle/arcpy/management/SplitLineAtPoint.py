# Generated documentation for module arcpy.management


class SplitLineAtPoint(object):
    """
    Splits line features based on intersection or proximity to point features.
    """

    @property
    def description(self) -> str:
        return """

        SplitLineAtPoint_management(in_features, point_features, out_feature_class, {search_radius})

        Splits line features based on intersection or proximity to point
        features.

     INPUTS:
      in_features (Feature Layer):
          The input line features that will be split.
      point_features (Feature Layer):
          The input point features whose locations will be used to split the
          input lines.
      search_radius {Linear Unit}:
          The distance that will be used to split lines by their proximity to
          point features. Points within the search distance to an input line
          will be used to split those lines at the nearest location to the point
          along the line segment.If this parameter is not specified, the single
          nearest point will be
          used to split the line feature. If a radius is specified, all points
          within the radius will be used to split the line.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will contain the split lines.

        """