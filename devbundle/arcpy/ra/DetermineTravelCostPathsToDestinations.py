# Generated documentation for module arcpy.ra


class DetermineTravelCostPathsToDestinations(object):
    """
    Calculates specific paths between known sources and known destinations.
    """

    @property
    def description(self) -> str:
        return """

        DetermineTravelCostPathsToDestinations_ra(inputDestinationRasterOrFeatures, inputCostDistanceRaster, inputCostBacklinkRaster, outputName, {destinationField}, {pathType})

        Calculates specific paths between known sources and known
        destinations.

     INPUTS:
      inputDestinationRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          An image service or feature service that identifies the cells from
          which the least-cost path is determined to the least costly source.If
          the input is an image service, the input consists of cells that
          have valid values (zero is a valid value), and the remaining cells
          must be assigned NoData.
      inputCostDistanceRaster (Image Service / Raster Layer / String):
          The name of a cost distance image service to be used to determine the
          least-cost path from the destination locations to a source.The cost
          distance raster is usually created with the Calculate Travel
          Cost tool. The cost distance raster stores, for each cell, the minimum
          accumulative cost distance over a cost surface from each cell to a set
          of source cells.
      inputCostBacklinkRaster (Image Service / Raster Layer / String):
          The name of a cost back link raster used to determine the path to
          return to a source via the least-cost path.For each cell in the back
          link raster, a value identifies the neighbor
          that is the next cell on the least accumulative cost path from the
          cell to a single source cell or set of source cells.
      outputName (String):
          The name of the output travel cost paths raster service.The default
          name is based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      destinationField {String}:
          A field on the destination layer that holds the values that define
          each destination.Input feature service must contain at least one valid
          field.
      pathType {String}:
          Defines the manner in which the values and zones on the input
          destination data will be interpreted in the cost path
          calculations.EACH_CELL-For each cell with valid values on the input
          destination
          data, a least-cost path is determined and saved on the output raster.
          With this option, each cell of the input destination data is treated
          separately, and a least-cost path is determined for each from cell.
          This is the default.EACH_ZONE-For each zone on the input destination
          data, a least-cost
          path is determined and saved on the output raster. With this option,
          the least-cost path for each zone begins at the cell with the lowest
          cost distance weighting in the zone.BEST_SINGLE-For all cells on the
          input destination data, the least-
          cost path is derived from the cell with the minimum of the least-cost
          paths to source cells.

        """