# Generated documentation for module arcpy.analysis


class Clip(object):
    """
    Extracts input features that overlay the clip features.
    """

    @property
    def description(self) -> str:
        return """

        Clip_analysis(in_features, clip_features, out_feature_class, {cluster_tolerance})

        Extracts input features that overlay the clip features.

     INPUTS:
      in_features (Feature Layer / Scene Layer / Building Scene Layer / File):
          The features that will be clipped.
      clip_features (Feature Layer):
          The features that will be used to clip the input features.
      cluster_tolerance {Linear Unit}:
          The minimum distance separating all feature coordinates as well as the
          distance a coordinate can move in x or y (or both). Set the value
          higher for data with less coordinate accuracy and lower for data with
          extremely high accuracy.Changing this parameter's value may cause
          failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.

     OUTPUTS:
      out_feature_class (Feature Class / File):
          The dataset that will be created.

        """