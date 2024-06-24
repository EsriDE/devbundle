# Generated documentation for module arcpy.aviation


class AddAviationLineBypass(object):
    """
    Adjusts route polyline features that overlap point features.
    """

    @property
    def description(self) -> str:
        return """

        AddAviationLineBypass_aviation(in_map, target_line_features, {bypass_features;bypass_features...}, {tolerance}, {radius_option}, {radius_scale}, {radius}, {merge_option})

        Adjusts route polyline features that overlap point features.

     INPUTS:
      in_map (Map):
          The input map with a set reference scale.
      target_line_features (String):
          The polyline features representing ATS routes.
      bypass_features {String}:
          The point features that the target_line_features parameter value will
          bypass.
      tolerance {Linear Unit}:
          The maximum distance between the center point of a bypass feature and
          a route.If the linear unit is not specified or is set to Unknown, it
          will be
          the same as the input map's spatial reference.
      radius_option {String}:
          Specifies the type of bypass radius that will be
          used.DYNAMIC_RADIUS-The radius will be dynamic relative to its scale
          factor. This is the default.CONSTANT_RADIUS-The radius will be a
          constant radius.
      radius_scale {Double}:
          The amount a bypass with a dynamic radius will be scaled. This
          parameter is only valid if DYNAMIC_RADIUS is chosen as the
          radius_option parameter value.
      radius {Linear Unit}:
          The radius of a bypass with a constant radius. This parameter is only
          valid if CONSTANT_RADIUS is chosen as the radius_option parameter
          value.If the linear unit is not specified or is set to Unknown, it
          will be
          the same as the input map's spatial reference.
      merge_option {String}:
          Specifies whether consecutive bypass lines will be
          merged.NO_MERGE_BYPASS-Consecutive bypass lines will not be merged.
          This is
          the default.MERGE_BYPASS-Consecutive bypass lines will be merged.

        """