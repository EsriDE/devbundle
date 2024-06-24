# Generated documentation for module arcpy.sa.Functions


class OptimalPathAsRaster(object):
    """
    Calculates the optimal path from a source to a destination as a raster.
    """

    @property
    def description(self) -> str:
        return """

        OptimalPathAsRaster_sa(in_destination_data, in_distance_accumulation_raster, in_back_direction_raster, {destination_field}, {path_type})

        Calculates the optimal path from a source to a destination as a
        raster.

     INPUTS:
      in_destination_data (Composite Geodataset):
          An integer raster or feature (point, line, or polygon) that identifies
          locations from which the optimal path will be determined to the least
          costly source.If the input is a raster, it must consist of cells that
          have valid
          values for the destinations, and the remaining cells must be assigned
          NoData. Zero is a valid value.
      in_distance_accumulation_raster (Composite Geodataset):
          The distance accumulation raster that will be used to determine the
          optimal path from the sources to the destinations.The distance
          accumulation raster is usually created with the Distance
          Accumulation or Distance Allocation tool. Each cell in the distance
          accumulation raster represents the minimum accumulative cost distance
          over a surface from each cell to a set of source cells.
      in_back_direction_raster (Composite Geodataset):
          The back direction raster contains calculated directions in degrees.
          The direction identifies the next cell along the optimal path back to
          the least accumulative cost source while avoiding barriers.The range
          of values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).
      destination_field {Field}:
          The field that will be used to obtain values for the destination
          locations.
      path_type {String}:
          Specifies a keyword defining the manner in which the values and zones
          on the input destination data will be interpreted in the cost path
          calculations.EACH_ZONE-For each zone on the input destination data, a
          least-cost
          path will be determined and saved on the output raster. With this
          option, the least-cost path for each zone begins at the cell with the
          lowest cost distance weighting in the zone.BEST_SINGLE-For all cells
          on the input destination data, the least-
          cost path will be derived from the cell with the minimum of the least-
          cost paths to source cells.EACH_CELL-For each cell with valid values
          on the input destination
          data, a least-cost path will be determined and saved on the output
          raster. With this option, each cell of the input destination data is
          treated separately, and a least-cost path is determined for each cell.

     OUTPUTS:
      out_path_accumulation_raster (Raster Dataset):
          The output raster.

        """