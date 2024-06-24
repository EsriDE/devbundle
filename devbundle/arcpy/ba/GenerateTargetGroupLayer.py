# Generated documentation for module arcpy.ba


class GenerateTargetGroupLayer(object):
    """
    Generates a layer that identifies geographies that contain selected segments and categorized groups based on targets.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTargetGroupLayer_ba(geography_level, segmentation_base, out_feature_class, target_group, {boundary_layer})

        Generates a layer that identifies geographies that contain selected
        segments and categorized groups based on targets.

     INPUTS:
      geography_level (String):
          The geography level that will be used to define the target layer.
      segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset in use.
      target_group (File):
          A user-created group of targets. This is used if the dataset supports
          target groups.
      boundary_layer {Feature Layer}:
          The boundary that determines the layer extent.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class for the target layer.

        """