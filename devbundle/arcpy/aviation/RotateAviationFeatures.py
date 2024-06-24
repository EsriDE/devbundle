# Generated documentation for module arcpy.aviation


class RotateAviationFeatures(object):
    """
    Aligns features to a grid or to the page.
    """

    @property
    def description(self) -> str:
        return """

        RotateAviationFeatures_aviation(in_map, target_layers;target_layers..., {rotate_option})

        Aligns features to a grid or to the page.

     INPUTS:
      in_map (Map):
          The map containing aviation features.
      target_layers (String):
          The point or annotation feature layers that will be rotated.
      rotate_option {String}:
          Specifies how the features will be rotated.ROTATE_TO_GRID-The features
          will be rotated to the map's grid. This is
          the default.ROTATE_TO_PAGE_TOP-The features will be rotated to the top
          of the
          page.ROTATE_TO_PAGE_LEFT-The features will be rotated to the left side
          of
          the page.ROTATE_TO_PAGE_BOTTOM-The features will be rotated to the
          bottom of
          the page.ROTATE_TO_PAGE_RIGHT-The features will be rotated to the
          right side of
          the page.

        """