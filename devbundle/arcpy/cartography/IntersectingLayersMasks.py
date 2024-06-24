# Generated documentation for module arcpy.cartography


class IntersectingLayersMasks(object):
    """
    Creates masking polygons at a specified shape and size at the intersection of two symbolized input layers: the masking layer and the masked layer.
    """

    @property
    def description(self) -> str:
        return """

        IntersectingLayersMasks_cartography(masking_layer, masked_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes)

        Creates masking polygons at a specified shape and size at the
        intersection of two symbolized input layers: the masking layer and the
        masked layer.

     INPUTS:
      masking_layer (Annotation Layer / Layer):
          The symbolized input layer that will intersect the masked layer to
          create masking polygons. This is the layer that will be displayed when
          masking is applied to the masked layer.
      masked_layer (Annotation Layer / Layer):
          The symbolized input layer that will be masked. This is the layer that
          will be obscured by the masking polygons.
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
          Margin values can be specified in either page units or map units. Most
          of the time margin distance values are specified in page units.The
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
          transferred to the output features. This is the default.NO_FID-All the
          attributes except the FID from the input features will
          be transferred to the output features.ALL-All the attributes from the
          input features will be transferred to
          the output features.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features.

        """