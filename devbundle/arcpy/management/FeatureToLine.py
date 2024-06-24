# Generated documentation for module arcpy.management


class FeatureToLine(object):
    """
    Creates a feature class containing lines generated by converting polygon boundaries to lines, or splitting line, polygon, or both features at their intersections.
    """

    @property
    def description(self) -> str:
        return """

        FeatureToLine_management(in_features;in_features..., out_feature_class, {cluster_tolerance}, {attributes})

        Creates a feature class containing lines generated by converting
        polygon boundaries to lines, or splitting line, polygon, or both
        features at their intersections.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon, or both.
      cluster_tolerance {Linear Unit}:
          The minimum distance separating all feature coordinates, and the
          distance a coordinate can move in X, Y, or both during spatial
          computation. The default XY tolerance is set to 0.001 meter or its
          equivalent in feature units.Changing this parameter's value may cause
          failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.
      attributes {Boolean}:
          Specifies whether to preserve or omit the input attributes in the
          output feature class.ATTRIBUTES-Preserves the input attributes in the
          output features. This
          is the default.NO_ATTRIBUTES-Omits the input attributes in the output
          features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class.

        """