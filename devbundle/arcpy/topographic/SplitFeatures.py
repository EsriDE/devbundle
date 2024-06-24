# Generated documentation for module arcpy.topographic


class SplitFeatures(object):
    """
    Splits features on input feature classes for any number of polyline or polygon target feature classes using the cutting features, and inserts points on the cutting feature.
    """

    @property
    def description(self) -> str:
        return """

        SplitFeatures_topographic(cutting_features, target_features;target_features..., use_target_z)

        Splits features on input feature classes for any number of polyline or
        polygon target feature classes using the cutting features, and inserts
        points on the cutting feature.

     INPUTS:
      cutting_features (Feature Layer):
          The cutting features that will be used to split the target features
          where they intersect the target feature class geometries.
      target_features (Feature Layer):
          The features that will be divided by the cutting features.
      use_target_z (Boolean):
          Specifies whether the z-value from the source or target will be
          used.USE_TARGET_Z-The z-value from the source or target will be
          used.DONT_USE_TARGET_Z-The z-value from the source or target will not
          be
          used. This is the default.

        """