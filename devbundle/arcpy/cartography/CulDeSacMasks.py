# Generated documentation for module arcpy.cartography


class CulDeSacMasks(object):
    """
    Creates a feature class of polygon masks from a symbolized input line layer.
    """

    @property
    def description(self) -> str:
        return """

        CulDeSacMasks_cartography(input_layer, output_fc, reference_scale, spatial_reference, margin, attributes)

        Creates a feature class of polygon masks from a symbolized input line
        layer.

     INPUTS:
      input_layer (Layer):
          The input line layer from which the masks will be created.
      reference_scale (Double):
          The reference scale used for calculating the masking geometry when
          masks are specified in page units. This is typically the reference
          scale of the map.
      spatial_reference (Spatial Reference):
          The spatial reference of the map in which the masking polygons will be
          created. This is not the spatial reference that will be assigned to
          the output feature class. It is the spatial reference of the map in
          which the masking polygons will be used, since the position of
          symbology may change when features are projected.
      margin (Linear Unit):
          The space in page units surrounding the symbolized input features used
          to create the mask polygons. Typically, masking polygons are created
          with a small margin around the symbol to improve visual appearance.
          Margin values are specified in either page units or map units. Most of
          the time, you will specify your margin distance value in page
          units.The margin cannot be negative.
      attributes (String):
          Specifies the attributes that will be transferred from the input
          features to the output features.ONLY_FID-Only the FID field from the
          input features will be
          transferred to the output features. This is the default.NO_FID-All the
          attributes except the FID from the input features will
          be transferred to the output features.ALL-All the attributes from the
          input features will be transferred to
          the output features.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features.

        """