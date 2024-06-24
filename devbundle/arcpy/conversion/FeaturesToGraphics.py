# Generated documentation for module arcpy.conversion


class FeaturesToGraphics(object):
    """
    Converts a feature layer's symbolized features into graphic elements in a graphics layer.
    """

    @property
    def description(self) -> str:
        return """

        FeaturesToGraphics_conversion(in_layer, out_layer, {exclude_features})

        Converts a feature layer's symbolized features into graphic elements
        in a graphics layer.

     INPUTS:
      in_layer (Feature Layer):
          The layer to convert to graphics.
      exclude_features {Boolean}:
          Specifies whether the converted features will be excluded using a
          query.EXCLUDE_FEATURES-The features will be excluded. This is the
          default.KEEP_FEATURES-The features will not be excluded; they will be
          preserved.

     OUTPUTS:
      out_layer (Graphics Layer):
          The graphics layer containing the converted graphic elements.

        """