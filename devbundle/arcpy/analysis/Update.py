# Generated documentation for module arcpy.analysis


class Update(object):
    """
    Computes the geometric intersection of the input features and update features. The attributes and geometry of the input features are updated by the update features in the output feature class.
    """

    @property
    def description(self) -> str:
        return """

        Update_analysis(in_features, update_features, out_feature_class, {keep_borders}, {cluster_tolerance})

        Computes the geometric intersection of the input features and update
        features. The attributes and geometry of the input features are
        updated by the update features in the output feature class.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer. The geometry type must be polygon.
      update_features (Feature Layer):
          The features that will be used to update the input features. The
          geometry type must be polygon.
      keep_borders {Boolean}:
          Specifies whether the boundary of the update polygon features will be
          kept.BORDERS-The outside border of the update_features parameter value
          will
          be kept in the out_feature_class parameter value. This is the
          default.NO_BORDERS-The outside border of the update_features parameter
          value
          will not be kept after it is inserted into the in_features. Item
          values of the update_features parameter value take precedence over
          in_features parameter value attributes.
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
          The feature class that will contain the results.

        """