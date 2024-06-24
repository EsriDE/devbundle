# Generated documentation for module arcpy.maritime


class GenerateCartographicLimits(object):
    """
    Converts polygon features to polylines and removes all segments coincident with the erase features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateCartographicLimits_maritime(input_polygons, erase_features;erase_features..., target_feature_class)

        Converts polygon features to polylines and removes all segments
        coincident with the erase features.

     INPUTS:
      input_polygons (Feature Layer):
          The polygon features that will be converted to polylines to create
          feature outlines where they are not coincident with the erase_features
          parameter value.
      erase_features (Feature Layer):
          The polyline features that will be used to identify coincident
          features in the input_polygons parameter value that will be removed
          from the target_feature_class parameter value.
      target_feature_class (Feature Layer):
          The feature class containing the cartographic limit features that will
          be converted.

        """