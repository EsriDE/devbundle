# Generated documentation for module arcpy.analysis


class Intersect(object):
    """
    Computes a geometric intersection of the input features. Features or portions of features that overlap in all layers or feature classes will be written to the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        Intersect_analysis(in_features;in_features..., out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})

        Computes a geometric intersection of the input features. Features or
        portions of features that overlap in all layers or feature classes
        will be written to the output feature class.

     INPUTS:
      in_features (Value Table):
          A list of the input feature classes or layers. When the distance
          between features is less than the cluster tolerance, the features with
          the lower rank will snap to the feature with the higher rank. The
          highest rank is 1. For more information, see Priority ranks and
          geoprocessing tools.
      join_attributes {String}:
          Specifies the attributes from the input features that will be
          transferred to the output feature class.ALL-All the attributes from
          the input features will be transferred to
          the output feature class. This is the default.NO_FID-All the
          attributes except the FID attribute from the input
          features will be transferred to the output feature class.ONLY_FID-Only
          the FID attribute from the input features will be
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
          output will be line. If one or more of the inputs are points, the
          output feature class will contain points. This is the default.LINE-The
          intersections returned will be line. This is only valid if
          none of the inputs are points.POINT-The intersections returned will be
          point. If the inputs are line
          or polygon, the output will be a multipoint feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.

        """