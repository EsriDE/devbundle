# Generated documentation for module arcpy.sa.Functions


class FlowLength(object):
    """
    Calculates the upstream or downstream distance, or weighted distance, along the flow path for each cell.
    """

    @property
    def description(self) -> str:
        return """

        FlowLength_sa(in_flow_direction_raster, {direction_measurement}, {in_weight_raster})

        Calculates the upstream or downstream distance, or weighted distance,
        along the flow path for each cell.

     INPUTS:
      in_flow_direction_raster (Composite Geodataset):
          The input raster that shows the direction of flow out of each cell.The
          flow direction raster can be created using the Flow Direction
          tool.
      direction_measurement {String}:
          The direction of measurement along the flow path.DOWNSTREAM-Calculates
          the downslope distance along the flow path, from
          each cell to a sink or outlet on the edge of the
          raster.UPSTREAM-Calculates the longest upslope distance along the flow
          path,
          from each cell to the top of the drainage divide.
      in_weight_raster {Composite Geodataset}:
          An optional input raster for applying a weight to each cell.If no
          weight raster is specified, a default weight of 1 will be
          applied to each cell. For each cell in the output raster, the result
          will be the number of cells that flow into it.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster that shows for each cell the upstream or downstream
          distance along a flow path.

        """