# Generated documentation for module arcpy.management


class FeatureToPoint(object):
    """
    Creates a feature class containing points generated from the centroids of the input features or placed within the input features.
    """

    @property
    def description(self) -> str:
        return """

        FeatureToPoint_management(in_features, out_feature_class, {point_location})

        Creates a feature class containing points generated from the centroids
        of the input features or placed within the input features.

     INPUTS:
      in_features (Feature Layer):
          The input features, which can be multipoint, line, polygon, or
          annotation.
      point_location {Boolean}:
          Specifies whether an output point will be located within the input
          feature or at the centroid of the input feature.CENTROID-The output
          point will be located at the centroid of the input
          feature. The output point may not always be contained by the input
          feature. This is the default.INSIDE-The output point will be located
          within the input feature. If the point_location parameter is
          set to CENTROID, the
          location of each output point will be determined as follows:
          Multipoint features-The output point will be located at the average x-
          and y-coordinate of all the points in the multipoint.Polyline
          features-The output point will be located at the weighted
          average x- and y-coordinate of the midpoints of all line segments in
          the line where the weight of a particular midpoint is the length of
          the correspondent line segment. Parametric (true) curves will be
          densified.Polygon features-The output point will be located at the
          center of
          gravity (centroid) of the polygon. If the point_location
          parameter is set to INSIDE, the location
          of the representative point of an input feature will be contained by
          the input feature and determined as follows:        Multipoint
          features-The output point will be coincident with one of
          the points in the multipoint.Polyline features-The output point will
          be on the line. If the line is
          a parametric (true) curve, the output point will be at the midpoint of
          the line.Polygon features-The output point will be inside the polygon.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class.

        """