# Generated documentation for module arcpy.sa.Functions


class FlowDistance(object):
    """
    Computes, for each cell, the horizontal or vertical component of downslope distance, following the flow paths, to cells on a stream into which they flow. In case of multiple flow paths, minimum, weighted mean, or maximum flow distance can be computed.
    """

    @property
    def description(self) -> str:
        return """

        FlowDistance_sa(in_stream_raster, in_surface_raster, {in_flow_direction_raster}, {distance_type}, {flow_direction_type}, {statistics_type})

        Computes, for each cell, the horizontal or vertical component of
        downslope distance, following the flow paths, to cells on a stream
        into which they flow. In case of multiple flow paths, minimum,
        weighted mean, or maximum flow distance can be computed.

     INPUTS:
      in_stream_raster (Composite Geodataset):
          An input stream raster that represents a linear stream network.
      in_surface_raster (Composite Geodataset):
          The input raster representing a continuous surface.
      in_flow_direction_raster {Composite Geodataset}:
          The input raster that shows the direction of flow out of each
          cell.When a flow direction raster is provided, the down slope
          direction(s)
          will be limited to those defined by the input flow directions.The flow
          direction raster can be created using the Flow Direction
          tool.The flow direction raster can be created using the D8, Multiple
          Flow
          Direction (MFD), or D-Infinity method. Use the flow_direction_type
          parameter to specify the method used when the flow direction raster
          was created.
      distance_type {String}:
          Determines if the vertical or horizontal component of flow distance is
          calculated.VERTICAL-The flow distance calculations represent the
          vertical
          component of flow distance, following the flow path, from each cell in
          the domain to cell(s) on the stream into which they flow. This is the
          default.HORIZONTAL-The flow distance calculations represent the
          horizontal
          component of flow distance, following the flow path, from each cell in
          the domain to cell(s) on the stream into which they flow.
      flow_direction_type {String}:
          Specifies the input flow direction raster type.D8-The input flow
          direction raster is of type D8. This is the
          default.MFD-The input flow direction raster is of type Multi Flow
          Direction
          (MFD).DINF-The input flow direction raster is of type D-Infinity
          (DINF).
      statistics_type {String}:
          Determines the statistics type used to compute flow distance over
          multiple flow paths. If there is only a single flow path from each
          cell to a cell on the stream, all statistics types produce the same
          result.MINIMUM-Where multiple flow paths exist, minimum flow distance
          in
          computed. This is the default.WEIGHTED_MEAN-Where multiple flow paths
          exist, a weighted mean of flow
          distance is computed. Flow proportion from a cell to its downstream
          neighboring cells are used as weights for computing weighted
          mean.MAXIMUM-When multiple flow paths exist, maximum flow distance is
          computed.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output flow distance raster.

        """