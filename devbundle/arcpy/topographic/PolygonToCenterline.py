# Generated documentation for module arcpy.topographic


class PolygonToCenterline(object):
    """
    Creates centerlines from polygon features. This tool is useful for creating centerlines from hydrographic polygons for use at smaller scales.
    """

    @property
    def description(self) -> str:
        return """

        PolygonToCenterline_topographic(in_features, out_feature_class, {connecting_features;connecting_features...})

        Creates centerlines from polygon features. This tool is useful for
        creating centerlines from hydrographic polygons for use at smaller
        scales.

     INPUTS:
      in_features (Feature Layer):
          The polygon features that will be used to create the centerline.
      connecting_features {Feature Layer}:
          The features that will be used to ensure connectivity of the
          centerline with other features in a network. The centerline will link
          to the point or the shared boundary wherever a feature from a
          connecting feature class touches the input feature.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class for the centerlines.

        """