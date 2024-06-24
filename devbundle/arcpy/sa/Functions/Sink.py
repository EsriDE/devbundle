# Generated documentation for module arcpy.sa.Functions


class Sink(object):
    """
    Creates a raster identifying all sinks or areas of internal drainage.
    """

    @property
    def description(self) -> str:
        return """

        Sink_sa(in_flow_direction_raster)

        Creates a raster identifying all sinks or areas of internal drainage.

     INPUTS:
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool, run using the default flow direction type D8.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster that shows all the sinks (areas of internal
          drainage) on the input surface.This output is of integer type.

        """