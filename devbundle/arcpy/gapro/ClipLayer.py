# Generated documentation for module arcpy.gapro


class ClipLayer(object):
    """
    Extracts input features from within specified polygons.
    """

    @property
    def description(self) -> str:
        return """

        ClipLayer_gapro(input_layer, clip_layer, out_feature_class)

        Extracts input features from within specified polygons.

     INPUTS:
      input_layer (Feature Layer):
          The dataset containing the point, line, or polygon features to be
          clipped.
      clip_layer (Feature Layer):
          The dataset containing the polygon features used to clip the input
          features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class with clipped features.

        """