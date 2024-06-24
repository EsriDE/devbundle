# Generated documentation for module arcpy.cartography


class FeatureOutlineMasks(object):
    """
    Creates mask polygons at a specified distance and shape around the symbolized features in the input layer.
    """

    @property
    def description(self) -> str:
        return """

        FeatureOutlineMasks_cartography(input_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes, {preserve_small_sized_features})

        Creates mask polygons at a specified distance and shape around the
        symbolized features in the input layer.

     INPUTS:
      input_layer (Annotation Layer / Layer):
          The symbolized input layer from which the masks will be created.
      reference_scale (Double):
          The reference scale that will be used for calculating the masking
          geometry when masks are specified in page units. This is typically the
          reference scale of the map.
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
          Margin values can be specified in either page units or map units.The
          margin cannot be negative.
      method (String):
          Specifies the type of masking geometry that will be created.BOX-A
          polygon representing the extent of the symbolized feature will
          be created.CONVEX_HULL-The convex hull of the symbolized geometry of
          the feature
          will be created. This is the default.EXACT_SIMPLIFIED-A generalized
          polygon representing the exact shape of
          the symbolized feature will be created. Polygons created with this
          method will have a significantly smaller number of vertices compared
          to polygons created with the EXACT option.EXACT-A polygon representing
          the exact shape of the symbolized feature
          will be created.
      mask_for_non_placed_anno (String):
          Specifies whether masks for unplaced annotation will be created. This
          parameter is only used when masking geodatabase annotation
          layers.ALL_FEATURES-Masks will be created for all annotation features.
          This
          is the default.ONLY_PLACED-Masks will only be created for features
          with a status of
          placed.
      attributes (String):
          Specifies the attributes that will be transferred from the input
          features to the output features.ONLY_FID-Only the FID field from the
          input features will be
          transferred to the output features. This is the default.NO_FID-All
          attributes except the FID field from the input features
          will be transferred to the output features.ALL-All attributes from
          the input features will be transferred to the
          output features.
      preserve_small_sized_features {Boolean}:
          Specifies whether small mask features will be included in the output
          feature class.DO_NOT_PRESERVE_SMALL_SIZED_FEATURES-Small mask features
          will not be
          included in the output feature class. This is the
          default.PRESERVE_SMALL_SIZED_FEATURES-All mask features will be
          included in
          the output feature class.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features.

        """