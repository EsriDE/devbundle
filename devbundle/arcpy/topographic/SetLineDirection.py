# Generated documentation for module arcpy.topographic


class SetLineDirection(object):
    """
    Sets the direction of line segments to match the slope direction of underlying elevation features. The direction of a line is used by some of the generalization and cartography tools.
    """

    @property
    def description(self) -> str:
        return """

        SetLineDirection_topographic(in_line_features, digital_elevation_model, {line_direction}, {reverse_direction}, {vertical_tolerance})

        Sets the direction of line segments to match the slope direction of
        underlying elevation features. The direction of a line is used by some
        of the generalization and cartography tools.

     INPUTS:
      in_line_features (Feature Layer):
          The line features that will be modified.
      digital_elevation_model (Raster Layer / Mosaic Layer):
          The input elevation surface that will be used to evaluate the
          in_line_features parameter value.
      line_direction {String}:
          Specifies how the direction of the line segments will be
          set.DOWNHILL-The line segment direction will be
          downhill.DOWNHILL_FLOW-The
          line segment direction will use a flow network
          created by the input line features and adopt the direction from high
          values to low values. This is the default.DOWNHILL_SPLIT_FLOW-The same
          as Downhill Flow, except that the line
          features may split at hill tops or junctions to ensure the direction
          of flow with regard to vertical tolerance. This option may create new
          features.
      reverse_direction {Boolean}:
          Specifies whether the line features will be reversed along the flow
          direction.KEEP_DIRECTION-The line direction will be maintained. This
          is the
          default.REVERSE_DIRECTION-The line direction will be reversed.
      vertical_tolerance {Linear Unit}:
          The minimum difference in elevation between raster values before they
          are considered equal. The default is 0 meters.

        """