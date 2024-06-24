# Generated documentation for module arcpy.sa.Functions


class StreamLink(object):
    """
    Assigns unique values to sections of a raster linear network between intersections.
    """

    @property
    def description(self) -> str:
        return """

        StreamLink_sa(in_stream_raster, in_flow_direction_raster)

        Assigns unique values to sections of a raster linear network between
        intersections.

     INPUTS:
      in_stream_raster (Composite Geodataset):
          An input raster that represents a linear stream network.
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool, run using the default flow direction type D8.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output stream link raster.This output is of integer type.

        """