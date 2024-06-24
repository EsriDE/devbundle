# Generated documentation for module arcpy.ba


class GenerateTargetLayer(object):
    """
    Creates a layer that identifies geographies that contain selected segments and geographies that do not contain selected segments.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTargetLayer_ba(geography_level, segmentation_base, out_feature_class, input_type, {target_group}, {target}, {segments;segments...}, {boundary_layer})

        Creates a layer that identifies geographies that contain selected
        segments and geographies that do not contain selected segments.

     INPUTS:
      geography_level (String):
          The geography level that will be used to define the target layer.
      segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset in use.
      input_type (String):
          Specifies whether target groups or segments will be
          used.USE_TARGET_GROUP-A group of targets will be
          used.SELECT_SEGMENTS-Segments will be used. One or more segments can
          make
          up a target.
      target_group {File}:
          The target group, if the dataset supports target groups.
      target {String}:
          A target from the selected target_group.
      segments {String}:
          Segments from the provided dataset.
      boundary_layer {Feature Layer}:
          The boundary that determines the layer extent.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class for the target layer.

        """