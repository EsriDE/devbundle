# Generated documentation for module arcpy.ca


class EightyTwentyAnalysis(object):
    """
    Conducts an 80/20 analysis of features and creates point clusters, lines, or polygons based on the number of associated incidents. The tool calculates a cumulative percentage field to identify the locations where incidents are disproportionately occurring.
    """

    @property
    def description(self) -> str:
        return """

        EightyTwentyAnalysis_ca(in_features, out_feature_class, {cluster_tolerance}, {out_fields;out_fields...}, {aggregation_method}, {in_comparison_features})

        Conducts an 80/20 analysis of features and creates point clusters,
        lines, or polygons based on the number of associated incidents. The
        tool calculates a cumulative percentage field to identify the
        locations where incidents are disproportionately occurring.

     INPUTS:
      in_features (Feature Layer):
          The input point features that will be used to create clusters, lines,
          or polygons.
      cluster_tolerance {Linear Unit}:
          The maximum distance separating points at which they will be
          considered part of the same cluster.If no cluster tolerance is
          specified, the tool will create a cluster
          where point features overlap.This parameter is enabled when the
          aggregation_method parameter is set
          to POINT_CLUSTER.
      out_fields {Field}:
          The fields from the input features that will be transferred to the
          output.
      aggregation_method {String}:
          Specifies how the input point features will be
          aggregated.POINT_CLUSTER-The input point features will be clustered.
          This is the
          default.CLOSEST_FEATURE-The input point features will be aggregated to
          the
          closest comparison polygon or line feature.
      in_comparison_features {Feature Layer}:
          The comparison input polygon or line feature class by which the
          in_features parameter value is aggregated.This parameter is enabled
          when the aggregation_method parameter is set
          to CLOSEST_FEATURE.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.When the aggregation_method parameter is set
          to POINT_CLUSTER, the
          output will be a point feature class.When the aggregation_method
          parameter is set to CLOSEST_FEATURE, the
          geometry type of the output will be the same as the
          in_comparison_features parameter value.

        """