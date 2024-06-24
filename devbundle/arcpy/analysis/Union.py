# Generated documentation for module arcpy.analysis


class Union(object):
    """
    Computes a geometric union of the input features. All features and their attributes will be written to the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        Union_analysis(in_features;in_features..., out_feature_class, {join_attributes}, {cluster_tolerance}, {gaps})

        Computes a geometric union of the input features. All features and
        their attributes will be written to the output feature class.

     INPUTS:
      in_features (Value Table):
          The input feature classes or layers. When the distance between
          features is less than the cluster tolerance, the features with the
          lower rank will snap to the feature with the higher rank. The highest
          rank is one. All of the input features must be polygons.
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
      gaps {Boolean}:
          Specifies whether a feature will be created for areas in the output
          that are completely enclosed by polygons. Gaps are areas in the
          output feature class that are completely
          enclosed by other polygons (created from the intersection of features
          or from existing holes in the input polygons). These areas are not
          invalid, but you can identify them for analysis. To identify the gaps
          in the output, set this parameter to NO_GAPS, and a feature will be
          created in these areas. To select these features, query the output
          feature class based on all the input feature'svalues being equal to
          -1. FIDGAPS-A feature will not be created for an area in the
          output that is
          completely enclosed by polygons. This is the default.
          NO_GAPS-A feature will be created for an area in the output
          that is completely enclosed by polygons. This feature will have no
          attribute values and will have avalue of -1. FID

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will contain the results.

        """