# Generated documentation for module arcpy.gapro


class OverlayLayers(object):
    """
    Overlays the geometries from multiple layers into a single layer. Overlay can be used to combine, erase, modify, or update spatial features.
    """

    @property
    def description(self) -> str:
        return """

        OverlayLayers_gapro(input_layer, overlay_layer, out_feature_class, overlay_type)

        Overlays the geometries from multiple layers into a single layer.
        Overlay can be used to combine, erase, modify, or update spatial
        features.

     INPUTS:
      input_layer (Feature Layer):
          The point, line, or polygon features that will be overlaid with the
          overlay layer.
      overlay_layer (Feature Layer):
          The features that will be overlaid with the input layer features.
      overlay_type (String):
          Specifies the type of overlay to be performed.INTERSECT-A geometric
          intersection of the input layers will be
          computed. Features or portions of features that overlap in both the
          input layer and overlay layer will be written to the output layer.
          This is the default.ERASE-Only those features or portions of features
          in the input layer
          that do not overlap the features in the overlay layer will be written
          to the output.UNION-A geometric union of the input layer and overlay
          layer will be
          computed. All features and their attributes will be written to the
          layer.IDENTITY-A geometric intersection of the input features and
          identity
          features will be computed. Features or portions of features that
          overlap in both the input layer and the overlay layer will be written
          to the output layer.SYMMETRICAL_DIFFERENCE-Features or portions of
          features in the input
          layer and overlay layer that do not overlap will be written to the
          output layer.

     OUTPUTS:
      out_feature_class (Feature Class):
          A new feature class with overlaid features.

        """