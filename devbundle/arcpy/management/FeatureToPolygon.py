# Generated documentation for module arcpy.management


class FeatureToPolygon(object):
    """
    Creates a feature class containing polygons generated from areas enclosed by input line or polygon features.
    """

    @property
    def description(self) -> str:
        return """

        FeatureToPolygon_management(in_features;in_features..., out_feature_class, {cluster_tolerance}, {attributes}, {label_features})

        Creates a feature class containing polygons generated from areas
        enclosed by input line or polygon features.

     INPUTS:
      in_features (Feature Layer):
          The input features, which can be line, polygon, or both.
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
          This parameter is no longer supported. The parameter remains
          for backward compatibility of scripts and models. See thesection for
          more information. Usage
      label_features {Feature Layer}:
          The optional input point features that contain the attributes to be
          transferred to the output polygon features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class.

        """