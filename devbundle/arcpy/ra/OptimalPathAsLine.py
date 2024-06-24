# Generated documentation for module arcpy.ra


class OptimalPathAsLine(object):
    """
    Calculates the optimal path from a source to a destination as a line.
    """

    @property
    def description(self) -> str:
        return """

        OptimalPathAsLine_ra(inputDestinationRasterOrFeatures, inputDistanceAccumulationRaster, inputBackDirectionRaster, outputPolylineName, {destinationField}, {pathType}, {createNetworkPaths})

        Calculates the optimal path from a source to a destination as a line.

     INPUTS:
      inputDestinationRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          A raster or feature dataset identifying locations from which the least
          accumulative cost path is determined to the least costly source.For a
          raster, the input type must be integer, and it must consist of
          cells that have valid values (zero is a valid value). The remaining
          cells must be assigned NoData. For a feature service, the input type
          can be point, line or polygon.
      inputDistanceAccumulationRaster (Image Service / Raster Layer / String):
          The distance accumulation raster is used to determine the optimal path
          from the sources to the destinations.The distance accumulation raster
          is usually created with the Distance
          Accumulation or Distance Allocation tool. Each cell in the distance
          accumulation raster represents the minimum accumulative cost distance
          over a surface from each cell to a set of source cells.
      inputBackDirectionRaster (Image Service / Raster Layer / String):
          The back direction raster contains calculated directions in degrees.
          The direction identifies the next cell along the optimal path back to
          the least accumulative cost source while avoiding barriers.The range
          of values is from 0 degrees to 360 degrees. The value 0 is
          reserved for the source cells. Due east (right) is 90 degrees, and the
          values increase clockwise (180 is south, 270 is west, and 360 is
          north).
      outputPolylineName (String):
          The name of the output feature service that contains the optimal
          paths.
      destinationField {String}:
          The field that will be used to obtain values for the destination
          locations.This field must be an integer.
      pathType {String}:
          Specifies a keyword defining the manner in which the values and zones
          in the input destination data will be interpreted in the cost path
          calculations.EACH_ZONE-For each zone in the input destination data, a
          least-cost
          path will be determined and saved on the output raster. With this
          option, the least-cost path for each zone begins at the cell with the
          lowest cost distance weighting in the zone. This is the
          default.BEST_SINGLE-For all cells in the input destination data, the
          least-
          cost path will be derived from the cell with the minimum of the least-
          cost paths to source cells.EACH_CELL-For each cell with valid values
          in the input destination
          data, a least-cost will be is determined and saved on the output
          raster. With this option, each cell of the input destination data is
          treated separately, and a least-cost path is determined for each cell.
      createNetworkPaths {Boolean}:
          Specifies whether complete, and possibly overlapping, paths from the
          destinations to the sources are calculated or if nonoverlapping
          network paths are created.DESTINATIONS_TO_SOURCES-Complete paths from
          the destinations to the
          sources are calculated, which can be overlapping. This is the
          default.NETWORK_PATHS-Nonoverlapping network paths are calculated.

        """