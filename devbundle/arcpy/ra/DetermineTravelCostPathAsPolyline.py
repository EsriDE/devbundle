# Generated documentation for module arcpy.ra


class DetermineTravelCostPathAsPolyline(object):
    """
    Calculates the least-cost polyline path between sources and destinations.
    """

    @property
    def description(self) -> str:
        return """

        DetermineTravelCostPathAsPolyline_ra(inputSourceRasterOrFeatures, inputCostRaster, inputDestinationRasterOrFeatures, outputPolylineName, {pathType}, {destinationField})

        Calculates the least-cost polyline path between sources and
        destinations.

     INPUTS:
      inputSourceRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          An image service or feature service that identifies the cells from
          which the least-cost path is determined to the destinations.If the
          input is an image service, the input consists of cells that
          have valid values (zero is a valid value), and the remaining cells
          must be assigned NoData.
      inputCostRaster (Image Service / Raster Layer / String):
          The name of a cost raster image service to be used to determine the
          least-cost path from the sources to the destinations.The value at each
          cell location represents the cost-per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      inputDestinationRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          An image service or feature service that identifies the cells to which
          the least-cost path is calculated.
      outputPolylineName (String):
          The name of the output polyline feature service.The polyline feature
          service of the optimum (least-cost) paths
          connecting sources and destinations. Each path (or line) is
          uniquely numbered, and has an
          additional field in the attribute table called, which connects it back
          to the unique identifier on the destination raster. DestIDSince
          each path is represented by a unique line, there can be multiple
          lines in locations where paths travel the same route.
      pathType {String}:
          Specifies the manner in which the values and zones on the input
          destination data will be interpreted in the cost path
          calculations.EACH_CELL-For each cell or location with valid values on
          the input
          destination data, a least-cost path is determined and saved on the
          output. With this option, each cell or location of the input
          destination data is treated separately, and a least-cost path is
          determined for each from cell.EACH_ZONE-For each zone on the input
          destination data, a least-cost
          path is determined and saved to the output. With this option, the
          least-cost path for each zone begins at the location with the lowest
          cost distance weighting in the zone.BEST_SINGLE-For all locations on
          the input destination data, the
          least-cost path is derived from the location with the minimum of the
          least-cost paths to source locations. This is the default.
      destinationField {String}:
          The field used to obtain values for the destination locations.Input
          feature data must contain at least one valid integer field.

        """