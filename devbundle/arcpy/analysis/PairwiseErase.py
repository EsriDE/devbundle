# Generated documentation for module arcpy.analysis


class PairwiseErase(object):
    """
    Computes a pairwise intersection of the input and erase features. Only those portions of the input features falling outside the erase features will be copied to the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        PairwiseErase_analysis(in_features, erase_features, out_feature_class, {cluster_tolerance})

        Computes a pairwise intersection of the input and erase features. Only
        those portions of the input features falling outside the erase
        features will be copied to the output feature class.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      erase_features (Feature Layer):
          The features that will be used to erase coincident features in the
          input.
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
          The output feature class.

        """