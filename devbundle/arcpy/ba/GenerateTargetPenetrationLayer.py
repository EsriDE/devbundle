# Generated documentation for module arcpy.ba


class GenerateTargetPenetrationLayer(object):
    """
    Generates a layer based on the percent of penetration of selected segments, providing a detailed view of the concentrations of your target segments.
    """

    @property
    def description(self) -> str:
        return """

        GenerateTargetPenetrationLayer_ba(geography_level, segmentation_base, out_feature_class, input_type, {target_group}, {target}, {segments;segments...}, {boundary_layer})

        Generates a layer based on the percent of penetration of selected
        segments, providing a detailed view of the concentrations of your
        target segments.

     INPUTS:
      geography_level (String):
          The geography level that will be used to define the target layer.
      segmentation_base (String):
          The segmentation base for the profile being created. Available options
          are provided by the segmentation dataset in use.
      input_type (String):
          The geographic layer containing the segmentation data or the target
          group.USE_TARGET_GROUP-A target group will be used as the input
          type.SELECT_SEGMENTS-Selected segments will be used as the input type.
          One
          or more segments can compose a target. This is the default.
      target_group {File}:
          A user-created group of targets. This parameter is used when the
          dataset supports target groups.
      target {String}:
          A target from the selected target_group.
      segments {String}:
          Segments from the provided dataset.
      boundary_layer {Feature Layer}:
          The boundary that determines the extent of the analysis.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class for the target layer.

        """