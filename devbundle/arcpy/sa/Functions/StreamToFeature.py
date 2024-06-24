# Generated documentation for module arcpy.sa.Functions


class StreamToFeature(object):
    """
    Converts a raster representing a linear network to features representing the linear network.
    """

    @property
    def description(self) -> str:
        return """

        StreamToFeature_sa(in_stream_raster, in_flow_direction_raster, out_polyline_features, {simplify})

        Converts a raster representing a linear network to features
        representing the linear network.

     INPUTS:
      in_stream_raster (Composite Geodataset):
          An input raster that represents a linear stream network.
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool.
      simplify {Boolean}:
          Specifies whether weeding is used.SIMPLIFY-The feature is weeded to
          reduce the number of vertices. The
          Douglas-Puecker algorithm for line generalization is used with a
          tolerance of sqrt(0.5) * cell size.NO_SIMPLIFY-No weeding is
          applied.By default, weeding is applied.

     OUTPUTS:
      out_polyline_features (Feature Class):
          Output feature class that will hold the converted streams.

        """