# Generated documentation for module arcpy.sa.Functions


class FlowDirection(object):
    """
    Creates a raster of flow direction from each cell to its downslope neighbor, or neighbors, using the D8, Multiple Flow Direction (MFD), or D-Infinity (DINF) method.
    """

    @property
    def description(self) -> str:
        return """

        FlowDirection_sa(in_surface_raster, {force_flow}, {out_drop_raster}, {flow_direction_type})

        Creates a raster of flow direction from each cell to its downslope
        neighbor, or neighbors, using the D8, Multiple Flow Direction (MFD),
        or D-Infinity (DINF) method.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input raster representing a continuous surface.
      force_flow {Boolean}:
          Specifies whether edge cells will always flow outward or follow normal
          flow rules.NORMAL-If the maximum drop on the inside of an edge cell is
          greater
          than zero, the flow direction will be determined as usual; otherwise,
          the flow direction will be toward the edge. Cells that should flow
          from the edge of the surface raster inward will do so. This is the
          default.FORCE-All cells at the edge of the surface raster will flow
          outward
          from the surface raster.
      flow_direction_type {String}:
          Specifies the type of flow method that will be used when computing
          flow directions.D8-Flow direction will be determined by the D8 method.
          This method
          assigns flow direction to the steepest downslope neighbor. This is the
          default.MFD-Flow direction will be based on the MFD flow method. Flow
          direction will be partitioned across downslope neighbors according to
          an adaptive partition exponent.DINF-Flow direction will be based on
          the DINF flow method. This method
          assigns flow direction to the steepest slope of a triangular facet.

     OUTPUTS:
      out_flow_direction_raster (Raster Dataset):
          The output raster that shows the flow direction from each cell to its
          downslope neighbors or neighbors using the D8, MFD, or DINF
          method.This output is of integer type.
      out_drop_raster {Raster Dataset}:
          An optional output drop raster.The drop raster returns the ratio of
          the maximum change in elevation
          from each cell along the direction of flow to the path length between
          centers of cells, expressed in percentages.This output is of floating-
          point type.

        """