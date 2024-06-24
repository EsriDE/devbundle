# Generated documentation for module arcpy.sa.Functions


class FlowAccumulation(object):
    """
    Creates a raster of accumulated flow into each cell. A weight factor can optionally be applied.
    """

    @property
    def description(self) -> str:
        return """

        FlowAccumulation_sa(in_flow_direction_raster, {in_weight_raster}, {data_type}, {flow_direction_type})

        Creates a raster of accumulated flow into each cell. A weight factor
        can optionally be applied.

     INPUTS:
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool.The flow direction raster can be created using the D8, Multiple
          Flow
          Direction (MFD), or D-Infinity method. Use the flow_direction_type
          parameter to specify the method used when the flow direction raster
          was created.
      in_weight_raster {Composite Geodataset}:
          An optional input raster for applying a weight to each cell.If no
          weight raster is specified, a default weight of 1 will be
          applied to each cell. For each cell in the output raster, the result
          will be the number of cells that flow into it.
      data_type {String}:
          The output accumulation raster can be integer, floating point, or
          double type.FLOAT-The output raster will be floating point type. This
          is the
          default.INTEGER-The output raster will be integer type.DOUBLE-The
          output raster will be double type.
      flow_direction_type {String}:
          Specifies the input flow direction raster type.D8-The input flow
          direction raster is of type D8. This is the
          default.MFD-The input flow direction raster is of type Multi Flow
          Direction
          (MFD).DINF-The input flow direction raster is of type D-Infinity
          (DINF).

     OUTPUTS:
      out_accumulation_raster (Raster Dataset):
          The output raster that shows the accumulated flow to each cell.

        """