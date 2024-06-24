# Generated documentation for module arcpy.analysis


class PairwiseIntersect(object):
    """
    Computes a pairwise intersection of the input features. Features or portions of features that overlap between the input feature layers or feature classes will be written to the output feature class. Pairwise intersection refers to selecting one feature from the first input and intersecting it with the features in the second input that it overlaps.
    """

    @property
    def description(self) -> str:
        return """

        PairwiseIntersect_analysis(in_features;in_features..., out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})

        Computes a pairwise intersection of the input features. Features or
        portions of features that overlap between the input feature layers or
        feature classes will be written to the output feature class. Pairwise
        intersection refers to selecting one feature from the first input and
        intersecting it with the features in the second input that it
        overlaps.

     INPUTS:
      in_features (Value Table):
          The input feature classes or layers to intersect. Only two inputs are
          allowed.
      join_attributes {String}:
          Specifies which attributes from the input features will be transferred
          to the output feature class.ALL-All the attributes from the input
          features will be transferred to
          the output feature class. This is the default.NO_FID-All the
          attributes except the FID from the input features will
          be transferred to the output feature class.ONLY_FID-Only the FID field
          from the input features will be
          transferred to the output feature class.
      cluster_tolerance {Linear Unit}:
          The minimum distance separating all feature coordinates (nodes and
          vertices) as well as the distance a coordinate can move in x or y (or
          both).Changing this parameter's value may cause failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.
      output_type {String}:
          Specifies the type of intersections that will be returned.INPUT-The
          intersections returned will be the same geometry type as the
          input features with the lowest dimension geometry. If all inputs are
          polygons, the output feature class will contain polygons. If one or
          more of the inputs are lines and none of the inputs are points, the
          output will be lines. If one or more of the inputs are points, the
          output feature class will contain points. This is the default.LINE-The
          intersections returned will be line. This is only valid if
          none of the inputs are points.POINT-The intersections returned will be
          point. If the inputs are line
          or polygon, the output will be a multipoint feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.

        """