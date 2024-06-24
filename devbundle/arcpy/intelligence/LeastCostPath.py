# Generated documentation for module arcpy.intelligence


class LeastCostPath(object):
    """
    Finds the shortest path between starting points and ending points across a cost surface.
    """

    @property
    def description(self) -> str:
        return """

        LeastCostPath_intelligence(in_cost_surface, in_start_point, in_end_point, out_path_feature_class, {handle_zeros})

        Finds the shortest path between starting points and ending points
        across a cost surface.

     INPUTS:
      in_cost_surface (Raster Layer):
          The input raster used to determine the cost to travel from starting
          point to ending point. No Data values cannot be crossed.
      in_start_point (Feature Set):
          The input starting point feature. Multiple start points will
          significantly increase processing time.
      in_end_point (Feature Set):
          The input ending point feature. Multiple end points will increase the
          number of output lines, as the resulting path will branch into
          separate paths.
      handle_zeros {String}:
          Specifies how zero values in the in_cost_surface parameter will be
          handled.SMALL_POSITIVE-All zeros will be changed to a small positive
          value.
          This will allow the cells to be traversed. This is the
          default.NO_DATA-All zeros will be changed to null values. The cells
          will not
          be traversed and will be avoided.

     OUTPUTS:
      out_path_feature_class (Feature Class):
          The output path feature class.

        """