# Generated documentation for module arcpy.sa.Functions


class DeriveContinuousFlow(object):
    """
    Generates a raster of accumulated flow into each cell from an input surface raster with no prior sink or depression filling required.
    """

    @property
    def description(self) -> str:
        return """

        DeriveContinuousFlow_sa(in_surface_raster, {in_depressions_data}, {in_weight_raster}, {out_flow_direction_raster}, {flow_direction_type}, {force_flow})

        Generates a raster of accumulated flow into each cell from an input
        surface raster with no prior sink or depression filling required.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input raster representing a continuous surface.
      in_depressions_data {Composite Geodataset}:
          An optional dataset that defines real depressions.The depressions can
          be defined either through a raster or a feature
          layer.If input is a raster, the depression cells must take a valid
          value,
          including zero, and the areas that are not depressions must be NoData.
      in_weight_raster {Composite Geodataset}:
          An optional input raster dataset that defines the fraction of flow
          that contributes to flow accumulation at each cell.The weight is only
          applied to the accumulation of flow.If no accumulation weight raster
          is specified, a default weight of 1
          will be applied to each cell.
      flow_direction_type {String}:
          Specifies the type of flow method that will be used when computing
          flow directions.D8-Flow direction will be determined by the D8 method.
          This method
          assigns flow direction to the steepest downslope neighbor. This is the
          default.MFD-Flow direction will be based on the MFD flow method. Flow
          direction will be partitioned across downslope neighbors according to
          an adaptive partition exponent.
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

     OUTPUTS:
      out_accumulation_raster (Raster Dataset):
          The output raster representing flow accumulation (number of upstream
          cells draining to each cell).The output raster is of floating-point
          type.
      out_flow_direction_raster {Raster Dataset}:
          The output raster that shows the direction of flow at each cell using
          the D8 or Multiple Flow Direction (MFD) method.The output is of
          integer type.

        """