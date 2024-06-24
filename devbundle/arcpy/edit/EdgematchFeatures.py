# Generated documentation for module arcpy.edit


class EdgematchFeatures(object):
    """
    Modifies input line features by spatially adjusting their shapes, guided by the specified edgematch links, so they become connected with the lines in the adjacent dataset.
    """

    @property
    def description(self) -> str:
        return """

        EdgematchFeatures_edit(in_features, in_link_features, {method}, {adjacent_features}, {border_features})

        Modifies input line features by spatially adjusting their shapes,
        guided by the specified edgematch links, so they become connected with
        the lines in the adjacent dataset.

     INPUTS:
      in_features (Feature Layer):
          The input line features that will be adjusted.
      in_link_features (Feature Layer):
          The input line features representing edgematch links.
      method {String}:
          Specifies the edgematch method that will be used to adjust input
          features only or input features and adjacent features to new
          connecting locations.MOVE_ENDPOINT-The endpoint of a line will be
          moved to the new
          connecting location. This is the default.ADD_SEGMENT-A straight
          segment will be added to the end of a line so
          it ends at the new connecting location.ADJUST_VERTICES-The endpoint of
          a line will be adjusted to the new
          connecting location. The remaining vertices will also be adjusted so
          that the positional changes are gradually reduced toward the opposite
          end of the line.
      adjacent_features {Feature Layer}:
          The line features that are adjacent to the input features. If
          provided, both the input and adjacent features will be adjusted to
          meet at new connecting locations, either the midpoints of the
          edgematch links or locations nearest to the midpoints of the links on
          the border features (if provided).
      border_features {Feature Layer}:
          The line or polygon features representing borders between the input
          and adjacent features. When you specify border features, both input
          and adjacent features will be adjusted to meet at new connecting
          locations nearest to the midpoints of the links on the border
          features.

        """