# Generated documentation for module arcpy.sa.Functions


class StreamOrder(object):
    """
    Assigns a numeric order to segments of a raster representing branches of a linear network.
    """

    @property
    def description(self) -> str:
        return """

        StreamOrder_sa(in_stream_raster, in_flow_direction_raster, {order_method})

        Assigns a numeric order to segments of a raster representing branches
        of a linear network.

     INPUTS:
      in_stream_raster (Composite Geodataset):
          An input raster that represents a linear stream network.The input
          stream raster linear network should be represented as values
          greater than or equal to one on a background of NoData.
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool, run using the default flow direction type D8.
      order_method {String}:
          The method used for assigning stream order.STRAHLER-The method of
          stream ordering proposed by Strahler in 1952.
          Stream order only increases when streams of the same order intersect.
          Therefore, the intersection of a first-order and second-order link
          will remain a second-order link, rather than creating a third-order
          link. This is the default.SHREVE-The method of stream ordering by
          magnitude, proposed by Shreve
          in 1967. All links with no tributaries are assigned a magnitude
          (order) of one. Magnitudes are additive downslope. When two links
          intersect, their magnitudes are added and assigned to the downslope
          link.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output stream order raster.This output is of integer type.

        """