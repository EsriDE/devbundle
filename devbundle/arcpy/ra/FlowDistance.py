# Generated documentation for module arcpy.ra


class FlowDistance(object):
    """
    Computes, for each cell, the horizontal or vertical component of downslope distance, following the flow paths, to cells on a stream into which they flow. In the case of multiple flow paths, minimum, weighted mean, or maximum flow distance can be computed.
    """

    @property
    def description(self) -> str:
        return """

        FlowDistance_ra(inputStreamRaster, inputSurfaceRaster, outputName, {inputFlowDirectionRaster}, {distanceType}, {flowDirectionType}, {statisticsType})

        Computes, for each cell, the horizontal or vertical component of
        downslope distance, following the flow paths, to cells on a stream
        into which they flow. In the case of multiple flow paths, minimum,
        weighted mean, or maximum flow distance can be computed.

     INPUTS:
      inputStreamRaster (Image Service / Raster Layer / String):
          The input raster that defines the stream network.
      inputSurfaceRaster (Image Service / Raster Layer / String):
          The input raster representing a continuous surface.
      outputName (String):
          The name of the output flow distance raster service.The default name
          is based on the tool name and the input layer name.
          If the layer name already exists, you will be prompted to provide
          another name.
      inputFlowDirectionRaster {Image Service / Raster Layer / String}:
          The input raster that shows the direction of flow out of each
          cell.When a flow direction raster is provided, the down slope
          direction(s)
          will be limited to those defined by the input flow directions.The flow
          direction raster can be created using the D8, MFD, or DINF
          method. Use the flowDirectionType parameter to specify the method used
          when the flow direction raster was created.
      distanceType {String}:
          The distance type to be calculated.VERTICAL-The flow distance
          calculations represent the vertical
          component of minimum flow distance, following the flow path, from each
          cell in the domain to cell(s) on the stream into which they flow. This
          is the default.HORIZONTAL-The flow distance calculations represent the
          horizontal
          component of minimum flow distance, following the flow path, from each
          cell in the domain to cell(s) on the stream into which they flow.
      flowDirectionType {String}:
          Specifies the input flow direction raster type.D8-The input flow
          direction raster is of type D8. This is the
          default.MFD-The input flow direction raster is of type Multi Flow
          Direction
          (MFD).DINF-The input flow direction raster is of type D-Infinity
          (DINF).
      statisticsType {String}:
          Determines the statistics type used to compute flow distance over
          multiple flow paths.If there exists only a single flow path from each
          cell to a cell on
          the stream, all statistics types produce the same result.MINIMUM-Where
          multiple flow paths exist, minimum flow distance is
          computed. This is the default.WEIGHTED_MEAN-Where multiple flow paths
          exist, a weighted mean of flow
          distance is computed. Flow proportion from a cell to its downstream
          neighboring cells is used as a weight for computing weighted
          mean.MAXIMUM-When multiple flow paths exist, maximum flow distance is
          computed.

        """