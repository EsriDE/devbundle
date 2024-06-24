# Generated documentation for module arcpy.analysis


class Identity(object):
    """
    Computes a geometric intersection of the input features and identity features. The input features or portions thereof that overlap identity features will get the attributes of those identity features.
    """

    @property
    def description(self) -> str:
        return """

        Identity_analysis(in_features, identity_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {relationship})

        Computes a geometric intersection of the input features and identity
        features. The input features or portions thereof that overlap identity
        features will get the attributes of those identity features.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      identity_features (Feature Layer):
          The identity feature class or layer. It must be polygon or the same
          geometry type as the input features.
      join_attributes {String}:
          Specifies how attributes will be transferred to the output feature
          class.ALL-All the attributes (including FIDs) from the input features,
          as
          well as the identity features, will be transferred to the output
          features. If no intersection is found, the identity feature values
          will not be transferred to the output (their values will be set to
          empty strings or 0) and the identity feature FID will be -1. This is
          the default.NO_FID-All the attributes except the FID from the input
          features and
          identity features will be transferred to the output features. If no
          intersection is found, the identity feature values will not be
          transferred to the output (their values will be set to empty strings
          or 0).ONLY_FID-All the attributes from the input features and only the
          FID
          from the identity features will be transferred to the output features.
          If no intersection is found, the identity features' FID attribute
          value in the output will be -1.
      cluster_tolerance {Linear Unit}:
          The minimum distance separating all feature coordinates (nodes and
          vertices) as well as the distance a coordinate can move in x or y (or
          both).Changing this parameter's value may cause failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.
      relationship {Boolean}:
          Specifies whether additional spatial relationships between the
          in_features and identity_features parameter values will be written to
          the output. This only applies when the geometry type of the
          in_features parameter value is line and the geometry type of the
          identity_features parameter value is polygon.NO_RELATIONSHIPS-No
          additional spatial relationship will be written to
          the output. KEEP_RELATIONSHIPS-The output line features will
          contain two
          additional fields,and. These fields contain the feature ID of the
          identity_features parameter value on the left and right side of the
          line feature. LEFT_polyRIGHT_poly

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be created and to which the results will
          be written.

        """