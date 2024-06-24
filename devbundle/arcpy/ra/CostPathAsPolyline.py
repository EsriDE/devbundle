# Generated documentation for module arcpy.ra


class CostPathAsPolyline(object):
    """
    Calculates the least-cost path from a source to a destination as a line feature.
    """

    @property
    def description(self) -> str:
        return """

        CostPathAsPolyline_ra(inputDestinationRasterOrFeatures, inputCostDistanceRaster, inputCostBacklinkRaster, outputPolylineName, {pathType}, {destinationField})

        Calculates the least-cost path from a source to a destination as a
        line feature.

     INPUTS:
      inputDestinationRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          An image service or feature service that identifies those locations
          from which the least-cost path is determined to the least costly
          source.If the input is an image service, the input consists of cells
          that
          have valid values (zero is a valid value), and the remaining cells
          must be assigned NoData.
      inputCostDistanceRaster (Image Service / Raster Layer / String):
          The cost distance or Euclidean distance raster to be used to determine
          the least-cost path from the sources to the destinations.
      inputCostBacklinkRaster (Image Service / Raster Layer / String):
          The name of the raster used to determine the path to return to a
          source via the least-cost path or the shortest path.For each cell in
          the back link or direction raster, a value identifies
          the neighbor that is the next cell on the path from the cell to a
          source cell.
      outputPolylineName (String):
          The output feature service that will contain the least cost path.
      pathType {String}:
          Specifies the manner in which the values and zones on the input
          destination data will be interpreted in the cost path
          calculations.BEST_SINGLE-For all cells on the input destination data,
          the least-
          cost path will be derived from the cell with the minimum of the least-
          cost paths to source cells.EACH_ZONE-For each zone on the input
          destination data, a least-cost
          path is determined and saved on the output raster. With this option,
          the least-cost path for each zone will begin at the cell with the
          lowest cost distance weighting in the zone.EACH_CELL-For each cell
          with valid values on the input destination
          data, a least-cost path is determined and saved on the output raster.
          With this option, each cell of the input destination data will be
          treated separately, and a least-cost path will be determined for each
          from cell.
      destinationField {String}:
          The field that will be used to obtain values for the destination
          locations.

        """