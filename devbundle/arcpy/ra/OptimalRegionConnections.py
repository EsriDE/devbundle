# Generated documentation for module arcpy.ra


class OptimalRegionConnections(object):
    """
    Calculates the optimal connection of paths between two or more input regions.
    """

    @property
    def description(self) -> str:
        return """

        OptimalRegionConnections_ra(inputRegionRasterOrFeatures, outputOptimalLinesName, {inputBarrierRasterOrFeatures}, {inputCostRaster}, {outputNeighborConnectionsName}, {distanceMethod}, {connectionsWithinRegions})

        Calculates the optimal connection of paths between two or more input
        regions.

     INPUTS:
      inputRegionRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          The input regions to be connected by the optimal network.Regions can
          be defined by either raster or feature data.If the region input is
          raster, the regions are defined by groups of
          contiguous (adjacent) cells of the same value. Each region must be
          uniquely numbered. The cells that are not part of any region must be
          NoData. The raster type must be integer, and the values can be either
          positive or negative.If the region input is feature data, it can be
          polygons, lines, or
          points. Polygon feature regions cannot be composed of multipart
          polygons.
      outputOptimalLinesName (String):
          The name of the output line feature service that connects each input
          region.Each path (or line) is uniquely numbered and additional fields
          in the
          attribute table store specific information about the path. Those
          additional fields are the following:PATHID-The unique identifier for
          the pathPATHCOST-The total
          accumulative distance or cost for the pathREGION1-The first region the
          path connectsREGION2-The other region the path connectsThis
          information provides insight into the paths within the network.Since
          each path is represented by a unique line, there will be
          multiple lines in locations where paths travel the same route.
      inputBarrierRasterOrFeatures {Image Service / Feature Layer / Raster Layer / String}:
          The dataset that defines the barriers.The barriers can be defined by
          an integer or a floating-point image
          service, or by a feature service. For a feature service, the input
          type can be point, line or polygon.For an image service barrier, the
          barrier must have a valid value,
          including zero, and the areas that are not barriers must be NoData.
      inputCostRaster {Image Service / Raster Layer / String}:
          An image service defining the impedance or cost to move
          planimetrically through each cell.The value at each cell location
          represents the cost-per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      outputNeighborConnectionsName {String}:
          The output polyline feature class identifying all paths from each
          region to each of its closest or cost neighbors.Each path (or line) is
          uniquely numbered and additional fields in the
          attribute table store specific information about the path. Those
          additional fields are the following:PATHID-The unique identifier for
          the pathPATHCOST-The total
          accumulative distance or cost for the pathREGION1-The first region the
          path connectsREGION2-The other region the path connectsThis
          information provides insight into the paths within the network
          and is useful when deciding which paths should be removed if
          necessary.Since each path is represented by a unique line, there will
          be
          multiple lines in locations where paths travel the same route.
      distanceMethod {String}:
          Specifies whether the distance will be calculated using a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.GEODESIC-The distance calculation will be performed on the
          ellipsoid.
          Regardless of input or output projection, the results will not change.
      connectionsWithinRegions {String}:
          Specifies whether the paths will continue and connect within the input
          regions.GENERATE_CONNECTIONS-Paths will continue within the input
          regions to
          connect all paths that enter a region.NO_CONNECTIONS-Paths will stop
          at the edges of the input regions and
          will not continue or connect within them.

        """