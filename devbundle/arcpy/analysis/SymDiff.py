# Generated documentation for module arcpy.analysis


class SymDiff(object):
    """
    Computes a geometric intersection of the input and update features, returning the input features and update features that do not overlap. Features or portions of features in the input and update features that do not overlap will be written to the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        SymDiff_analysis(in_features, update_features, out_feature_class, {join_attributes}, {cluster_tolerance})

        Computes a geometric intersection of the input and update features,
        returning the input features and update features that do not overlap.
        Features or portions of features in the input and update features that
        do not overlap will be written to the output feature class.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      update_features (Feature Layer):
          The update feature class or layer. The geometry type must be the same
          as that of the input feature class or layer.
      join_attributes {String}:
          Specifies the attributes that will be transferred to the output
          feature class.ALL-All the attributes from the input features will be
          transferred to
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

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to which the results will be written.

        """