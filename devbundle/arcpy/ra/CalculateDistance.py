# Generated documentation for module arcpy.ra


class CalculateDistance(object):
    """
    Calculates the Euclidean distance from a single source or set of sources.
    """

    @property
    def description(self) -> str:
        return """

        CalculateDistance_ra(inputSourceRasterOrFeatures, outputDistanceName, {maximumDistance}, {outputCellSize}, {outputDirectionName}, {outputAllocationName}, {allocationField}, {distanceMethod}, {inputBarrierRasterOrFeatures}, {outputBackDirectionName})

        Calculates the Euclidean distance from a single source or set of
        sources.

     INPUTS:
      inputSourceRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          The layer that defines the sources to calculate the distance to. The
          layer can be image service or feature service.For image service, the
          input type can be integer or floating point.For feature service, the
          input can be point, line or polygon.
      outputDistanceName (String):
          The name of the output distance raster service.
      maximumDistance {Linear Unit}:
          The maximum distance to calculate out to.The unit values are
          Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.The default units are meters.
      outputCellSize {Linear Unit}:
          Set the cell size and units for the output raster.The unit values are
          Kilometers, Meters, MilesInt, YardsInt, FeetInt,
          Miles, Yards, and Feet.The default units are meters.
      outputDirectionName {String}:
          The name of the output direction raster service.
      outputAllocationName {String}:
          The name of the output allocation raster service.
      allocationField {String}:
          A field on the source input that holds the values that define each
          source. It must be of type integer.
      distanceMethod {String}:
          Specifies whether to calculate the distance using a planar (flat
          earth) or a geodesic (ellipsoid) method.Planar-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.Geodesic-The distance calculation will be performed on the
          ellipsoid.
          Therefore, regardless of input or output projection, the results do
          not change.
      inputBarrierRasterOrFeatures {Image Service / Feature Layer / Raster Layer / String}:
          Dataset that defines the barriers.The barriers can be defined by an
          integer or floating point raster, or
          a feature layer.
      outputBackDirectionName {String}:
          The name of the output back direction raster service.

        """