# Generated documentation for module arcpy.management


class FeatureVerticesToPoints(object):
    """
    Creates a feature class containing points generated from specified vertices or locations of the input features.
    """

    @property
    def description(self) -> str:
        return """

        FeatureVerticesToPoints_management(in_features, out_feature_class, {point_location})

        Creates a feature class containing points generated from specified
        vertices or locations of the input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon.
      point_location {String}:
          Specifies where an output point will be created.ALL-A point will be
          created at each input feature vertex. This is the
          default.MID-A point will be created at the midpoint, not necessarily a
          vertex,
          of each input line or polygon boundary.START-A point will be created
          at the start point (first vertex) of
          each input feature.END-A point will be created at the end point (last
          vertex) of each
          input feature.BOTH_ENDS-Two points will be created, one at the start
          point and
          another at the endpoint of each input feature.DANGLE-A dangle point
          will be created for any start or end point of an
          input line, if that point is not connected to another line at any
          location along that line. This option does not apply to polygon input.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class.

        """