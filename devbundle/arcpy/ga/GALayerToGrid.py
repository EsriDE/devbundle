# Generated documentation for module arcpy.ga


class GALayerToGrid(object):
    """
    Exports a Geostatistical layer to a raster.
    """

    @property
    def description(self) -> str:
        return """

        GALayerToGrid_ga(in_geostat_layer, out_surface_grid, {cell_size}, {points_per_block_horz}, {points_per_block_vert})

        Exports a Geostatistical layer to a raster.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.
      points_per_block_horz {Long}:
          The number of predictions for each cell in the horizontal direction
          for block interpolation. The default is 1.
      points_per_block_vert {Long}:
          The number of predictions for each cell in the vertical direction for
          block interpolation. The default is 1.

     OUTPUTS:
      out_surface_grid (Raster Dataset):
          The raster to be created.

        """