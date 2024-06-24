# Generated documentation for module arcpy.cartography


class AggregatePoints(object):
    """
    Creates polygon features around clusters of proximate point features.
    """

    @property
    def description(self) -> str:
        return """

        AggregatePoints_cartography(in_features, out_feature_class, aggregation_distance)

        Creates polygon features around clusters of proximate point features.

     INPUTS:
      in_features (Feature Layer):
          The input point features that will be assessed for proximity and
          clustering.
      aggregation_distance (Linear Unit):
          The distance between points that will be clustered.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class created to hold the polygons that represent the
          point clusters.

        """